import rubrik_cdm

rubrik = rubrik_cdm.Connect()

sla_name = "PythonSDK"
hourly_frequency = 1
hourly_retention = 24
daily_frequency = 1
daily_retention = 30
monthly_frequency = 1
monthly_retention = 12
yearly_frequency = 1
yearly_retention = 5
archive_name = "AWS-S3-Bucket"
retention_on_brik_in_days = 15
instant_archive = True
starttime_hour = 0
starttime_min = 19
duration_hours = 12
replication_target = "REPLCLUSTER"
replication_retention_in_days =  30

# update replication target
update_sla = rubrik.update_sla(
    name=sla_name,
    replication_target=replication_target,
    replication_retention_in_days=replication_retention_in_days
)

print(update_sla)

# remove replication target
replication_target = "REMOVE"

update_sla = rubrik.update_sla(
    name=sla_name,
    replication_target=replication_target
)


print(update_sla)

# update hourly retention
hourly_frequency = 2
hourly_retention = 48

update_sla = rubrik.update_sla(
    name=sla_name,
    hourly_frequency=hourly_frequency,
    hourly_retention=hourly_retention
)

print(update_sla)