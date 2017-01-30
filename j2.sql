select * from
	(select vm.name,vm.instance_name,vm.host_id,nic.network_id from vm_instance as vm 
		left join 
			nics as nic on vm.id = nic.instance_id where vm.hypervisor_type = 'VMware' and vm.host_id is not NULL and vm.type in ('DomainRouter')) as q1 

left join
	(select vm.name,vm.instance_name,vm.host_id,nic.network_id from vm_instance as vm 
		left join 
			nics as nic on vm.id = nic.instance_id where vm.hypervisor_type = 'VMware' and vm.host_id is not NULL and vm.type not in ('DomainRouter')) as q2 

on q1.host_id = q2.host_id and q1.network_id = q2.network_id;

