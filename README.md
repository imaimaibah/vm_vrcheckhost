概要
========

このスクリプトは同じネットワークに所属しているVMとVRが同じHost上で起動している場合にその情報をファイルに出力する。  
マイグレーション対象のVMをログに出力のみ。通知は監視サーバ等と連携する必要がある。  
過去に同一VMがアラートとして通知されていた場合はそのVMは通知対象から一定時間(Cronによる指定実行回数)除外。

機能
=============

下記のSQLを実行し、結果をデータ化。
世代数(Default:5)分を遡って、同じVMがあるかチェックする。
過去に同じVMがない場合はログへアラートを出力する。

***トリガー:***  
実行はCronによる定期実行とする。

***オプション:***  
引数指定で世代数(Retension)を設定できるようにする。

***SQL:***  
下記のSQLより取得した結果を元にデータを形成。オプションにより指定の世代数分残してJSON形式で結果を保存。
```
select * from
        (select vm.name,vm.instance_name,vm.host_id,nic.network_id from vm_instance as vm
                left join
                        nics as nic on vm.id = nic.instance_id where vm.hypervisor_type = 'VMware' and vm.host_id is not NULL and vm.type in ('DomainRouter')) as q1

left join
        (select vm.name,vm.instance_name,vm.host_id,nic.network_id from vm_instance as vm
                left join
                        nics as nic on vm.id = nic.instance_id where vm.hypervisor_type = 'VMware' and vm.host_id is not NULL and vm.type not in ('DomainRouter')) as q2

on q1.host_id = q2.host_id and q1.network_id = q2.network_id;
```

***保存履歴のデータフォーマット(JSON):***  
保存履歴はファイルで保存する。  
データフォーマットは以下。
データは古い順にソートして保存。

```
{
      <unixtime>: {
        vr1_id: {
          network_id: <NETWORKID>
          host_id: <HOSTID>
          VM: [vm_id1, vm_id2, vm_id3,....]
        },
        vr2_id: {
          network_id: <NETWORKID>
          host_id: <HOSTID>
          VM: [vm_id4, vm_id5, vm_id6,....]
        },
                        ・
                        ・
                        ・
                        ・
        vrX_id: {
          network_id: <NETWORKID>
          host_id: <HOSTID>
          VM: [vm_idX, vm_idY, vm_idZ,....]
        },
      }
}
```

***ログフォーマット***  
ログフォーマットは以下(2月3日時点参考)。(英語)  
ログファイル名はスクリプト内に記載。
```
YYYY-MM-DD HH:MM:SS <vm_id1> is running on the same host where <vr1_id>.
YYYY-MM-DD HH:MM:SS <vm_id2> is running on the same host where <vr1_id>.
YYYY-MM-DD HH:MM:SS <vm_id3> is running on the same host where <vr1_id>.
```
マイグレーション対象毎にログを1行出力する。
上記のフォーマット例ではvm_id1、vm_id2、vm_id3がマイグレーションの対象となる。

利用方法  
==========
python -m vm_vrAlert `<num>`

`<num>`は世代数を指定。デフォルトで5世代残す。

パラメータはvm_vrAlert.pyファイル内に`jsonFile`,`outputLog`と定義。  
それぞれの説明は以下。

`jsonFile` = 過去の結果を世代数分記録するためのファイル。  
`outputLog` =  ログの吐き出し先 。  

Coding Policy  
=============

インデントはTabを使用する。  
変数名、関数名、クラス名にはCamel方式を採用。英語の単語を使用する。  
変数名は名詞で開始。名詞単語の区切りには(アンダースコア)で区切る事とする。  
クラス名、関数名(Method)は動詞で開始する。  


ファイル一覧
============
vm_vrAlert.py  
format_json.py  



クラス/メソッド  
============
***Main***  
==ファイル名: vm_vrAlert.py==


***SQL Execution***  
==ファイル名: exec_sql.py==  

***JSON format output***  
ファイル名: format_json.py  

***LogWrite***  
ファイル名: log_write.py  

制限事項
===========
以下の制限事項が存在する。
* 対象VMが履歴にあるかないかでログ出力の有無を判断しているため指定されている保存期間内で同じVMが対象になるとアラート出力しない。
    * 例)対象であるVMをマイグレートし、対処した後に何らかの原因でまた同じVMが再度マイグレーション対象となった場合、保存期間がすぎるまでアラート出力されない。したがって長く設定し過ぎると検知がおくれるので注意が必要。
