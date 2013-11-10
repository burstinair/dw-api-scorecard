main_begin()

#
sql = ```
    select 
```%(g.BATCH_CAL_DT)
generate_mail("", '', '项,值', 'left', sql, 700)

#业务
sql = ```
    select 
```%(g.BATCH_CAL_DT)
generate_mail("", '', '项,值', 'left', sql, 700)

#定位
sql = ```
    select 
```%(g.BATCH_CAL_DT)
generate_mail("", '', '项,值', 'left', sql, 700)

#端到端响应时间
sql = ```

```%(g.BATCH_CAL_DT)
generate_mail("端到端响应时间", '', '访问路径,访问次数,平均响应时间(ms)', 'left', sql, 700)

#端到端响应时间的PV分布
sql = ```

```%(g.BATCH_CAL_DT)
generate_mail("端到端响应时间的PV分布", '', '平均响应时间(ms),每Session访问次数,Session数,Session数占比,访问次数,访问次数占比', 'left', sql, 700)

#定位时间的PV分布
sql = ```

```%(g.BATCH_CAL_DT)
generate_mail("定位时间的PV分布", '', '平均响应时间(ms),每Session访问次数,Session数,Session数占比,访问次数,访问次数占比,访问次数小于等于2的Session数,访问次数小于等于2的Session数占比', 'left', sql, 700)

mail_end()

sendEmail(['zhongkai.zhao@dianping.com'], [], [], "移动API月报", g.HTML_TEXT)
