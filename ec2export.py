#!/usr/bin/env python

# Ramzi Sh Alqrainy

import boto
from boto import ec2

csv_file = open('aws_instances.csv','w+')

def process_instance_list(connection):
  map(build_instance_list,connection.get_all_instances())

def build_instance_list(reservation):
  map(write_instances,reservation.instances)

def write_instances(instance):
  service = '-'
  if 'Service' in instance.tags:
    service = instance.tags['Service']

  csv_file.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n"%(instance.id,instance.tags['Name'], service,instance.private_ip_address,
                                                            instance.state,instance.placement,instance.architecture, instance.vpc_id, instance.kernel, instance.instance_type, instance.image_id,instance.launch_time))
  csv_file.flush()



if __name__=="__main__":
  connection = boto.ec2.connect_to_region('XXXXXX',aws_access_key_id='XXXXXXXXXXXXX',aws_secret_access_key='XXXXXXXXXXXXXXXX')

process_instance_list(connection)

csv_file.close()

