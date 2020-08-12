# update_sla

Create a new SLA Domain.

```py
def update_sla(self, name, hourly_frequency=None, hourly_retention=None, daily_frequency=None, daily_retention=None, monthly_frequency=None, monthly_retention=None, yearly_frequency=None, yearly_retention=None, archive_name=None, retention_on_brik_in_days=None, instant_archive=False, timeout=15):  # pylint: ignore
```

## Arguments

| Name | Type | Description                     | Choices |
|------|------|---------------------------------|---------|
| name | str  | The name of the new SLA Domain. |         |

## Keyword Arguments

| Name                          | Type | Description                                                                                                                                 | Choices | Default |
|-------------------------------|------|---------------------------------------------------------------------------------------------------------------------------------------------|---------|---------|
| hourly_frequency              | int  | Hourly frequency to take backups.                                                                                                           |         | None    |
| hourly_retention              | int  | Number of hours to retain the hourly backups.                                                                                               |         | None    |
| daily_frequency               | int  | Daily frequency to take backups.                                                                                                            |         | None    |
| daily_retention               | int  | Number of hours to retain the daily backups.                                                                                                |         | None    |
| monthly_frequency             | int  | Monthly frequency to take backups.                                                                                                          |         | None    |
| monthly_retention             | int  | Number of hours to retain the monthly backups.                                                                                              |         | None    |
| yearly_frequency              | int  | Yearly frequency to take backups.                                                                                                           |         | None    |
| yearly_retention              | int  | Number of hours to retain the yearly backups.                                                                                               |         | None    |
| archive_name                  | str  | The optional archive location you wish to configure on the SLA Domain. Keyword `REMOVE` will remove the currently set archive location. When populated, you must also provide a `retention_on_brik_in_days` unless `REMOVE` is set. |         | None    |
| retention_on_brik_in_days     | int  | The number of days you wish to keep the backups on the Rubrik cluster. When populated, you must also provide a `archive_name`.              |         | None    |
| instant_archive               | int  | Flag that determines whether or not to enable instant archive. Set to true to enable.                                                       |         | False   |
| starttime_hour                | int  | (CDM 5.0+) Starting hour of allowed backup window. When populated, you must also provide `starttime_min` and `duration_hours`.              |         | None    |
| starttime_min                 | int  | (CDM 5.0+) Starting minute of allowed backup window. When populated, you must also provide a `starttime_hour` and `duration_hours`.         |         | None    |
| duration_hours                | int  | (CDM 5.0+) Length of allowed backup window. When populated, you must also provide both `startime_min` and `starttime_hour`.                 |         | None    |
| replication_target            | str  | (CDM 5.0+) (CDM 5.0+) Name of the replication target cluster. Keyword `REMOVE` will remove the currently set replication target from the SLA. When populated, you must also provide `replication_retention_in_days` unless `REMOVE` is set.           |         | None    |
| replication_retention_in_days | int  | (CDM 5.0+) Number of days to retain backup on target cluster. When populated, you must also provide `replication_target`.                   |         | None    |
| timeout                       | str  | The number of seconds to wait to establish a connection the Rubrik cluster before returning a timeout error.                                |         | 30      |

## Returns

| Type | Return Value                                                                                     |
|------|--------------------------------------------------------------------------------------------------|
| str  | No change required. The 'name' SLA Domain is already configured with the provided configuration. |
| dict | The full API response for `POST /v1/sla_domain`.                                                 |
| dict | The full API response for `POST /v2/sla_domain`.                                                 |

## Example


```py
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
```

