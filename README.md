## Overview

同じネットワークIDを持つVMとVRが同じホスト上で起動している場合にログを出力する.

このスクリプトは同じネットワークに所属しているVMとVRが同じHost上で起動している場合にその情報をファイルに出力する。

## Specification

*** トリガー: ***  
実行はCronによる定期実行とする。

*** オプション: ***  
引数指定で世代数(Retension)を設定できるようにする。


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

JSONのデータフォーマットは以下。
```
{
      <date+time>: {
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

ログフォーマットは以下(2月3日時点参考)。(英語)
```
YYYY-MM-DD HH:MM:SS <vm_id1> is running on the same host as <vr1_id>.
YYYY-MM-DD HH:MM:SS <vm_id2> is running on the same host as <vr1_id>.
YYYY-MM-DD HH:MM:SS <vm_id3> is running on the same host as <vr1_id>.
```
マイグレーション対象毎にログを1行出力する。
上記のフォーマット例ではvm_id1、vm_id2、vm_id3がマイグレーションの対象となる。

## How to use  

## Coding Policy  

Camel方式を採用。英語の単語を使用する。  
Varriablesは名詞で開始。名詞単語の区切りには(アンダースコア)で区切る事とする。  
Function(Method)は動詞で開始。    
条件文の中でReturnを実施しない事とする。  



## Class/Method  
