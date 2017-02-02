***Overview***

同じネットワークIDを持つVMとVRが同じホスト上で起動している場合にログを出力する.

このスクリプトは同じネットワークに所属しているVMとVRが同じHost上で起動している場合にその情報をファイルに出力する。

***Specification***

トリガー:
実行はCronによる定期実行とする。

下記のSQLより取得した結果を元にJSON形式で結果を保存。引数指定で世代数(Retension)を設定できるようにする。

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

***How to use***

***Coding Policy***

Camel方式を採用。基本的には英語の単語を使用。  
Varriablesは名詞で開始。名詞単語の区切りには(アンダースコア)で区切る事とする。  
Function(Method)は動詞で開始。    
Functionでは基本的に条件文の中でReturnを実施しない事とする。  

***Class/Method***
