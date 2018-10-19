import qingcloud.iaas
conn = qingcloud.iaas.connect_to_zone(
 'LFRZ1', # 你的资源所在的节点ID，可在控制台切换节点的地方查看，如 'pek1', 'pek2', 'gd1' 等
 'BGXPSXMWJLTAYLFKBDPE',
 'Kjf2nCzzMuRrHXV0VpuXSZhoMktLTuzXgrPzsozV',
 False
 )
# S2_SAN = conn.create_s2_shared_target('s2-gc06gggz','demo','ISCSI')
# S2_SAN = conn.delete_s2_shared_targets(['s2st-3zjq10uc'])
# S2_SAN = conn.update_s2_servers (['s2-2jpkus9q'])

# S2_SAN = conn.poweron_s2_servers (['s2-y5ebtb1y'])
# s2 = conn.resize_s2_servers(['s2-ugg5bxwt'],0)

# s2 = conn.delete_s2_servers(['s2-9mhc1ws8'])
# conn = qingcloud.iaa
#
# s.connect_to_zone('LFRZ1', 'IVOTQNMTWIMUGVNHLCXO', 'rdLSUZ1cg8gGsLVudRsTvCqYpZB2iGNakycpATZv',False )[

# s2 = conn.create_s2_server('vxnet-gpg65hc','vsan')
# sta = 'active'
# print(sta)
# s2 = conn.describe_s2_servers(status=[sta])
# s2 = conn.describe_s2_servers(s2_servers=['s2-5cq2vhof'])


s2 = conn.modify_s2_server('s2-5cq2vhof','test2')



