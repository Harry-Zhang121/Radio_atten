# Radio_atten

## Important notes

- [Oracle Instant Client](https://www.oracle.com/database/technologies/instant-client/winx64-64-downloads.html) need to be installed.

- Oracle Instant Client require [Visual studio C++ Redistributable](https://learn.microsoft.com/en-US/cpp/windows/latest-supported-vc-redist?view=msvc-170)



## Filter HopperManager text file

Use this regex.
This will extract v_level to group1, time and date to group2 and e_level to group3. 

```
(?:InterfacRx.+)(-\d{2})(?:\sdBm\s{3})(\d{2}:\d{2}:\d{2}\s\d{2}-\d{2}-\d{4})(?:\n.+)(-\d{2})
```

## Oracle database nonsence

I used TIMESTAMP data type for storing date and time.
To convert time and date sting from HopperManager to TIMESTAMP use `TO_TIMESTAMP` function

``` sql
insert into DATA(TIMESTAMP)
VALUES(to_timestamp('10:05:46 04-11-2022', 'HH24:MI:SS DD-MM-YYYY'))
```