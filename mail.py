main_begin()

#
sql = ```
    select 
```%(g.BATCH_CAL_DT)
generate_mail("", '', '��,ֵ', 'left', sql, 700)

#ҵ��
sql = ```
    select 
```%(g.BATCH_CAL_DT)
generate_mail("", '', '��,ֵ', 'left', sql, 700)

#��λ
sql = ```
    select 
```%(g.BATCH_CAL_DT)
generate_mail("", '', '��,ֵ', 'left', sql, 700)

#�˵�����Ӧʱ��
sql = ```

```%(g.BATCH_CAL_DT)
generate_mail("�˵�����Ӧʱ��", '', '����·��,���ʴ���,ƽ����Ӧʱ��(ms)', 'left', sql, 700)

#�˵�����Ӧʱ���PV�ֲ�
sql = ```

```%(g.BATCH_CAL_DT)
generate_mail("�˵�����Ӧʱ���PV�ֲ�", '', 'ƽ����Ӧʱ��(ms),ÿSession���ʴ���,Session��,Session��ռ��,���ʴ���,���ʴ���ռ��', 'left', sql, 700)

#��λʱ���PV�ֲ�
sql = ```

```%(g.BATCH_CAL_DT)
generate_mail("��λʱ���PV�ֲ�", '', 'ƽ����Ӧʱ��(ms),ÿSession���ʴ���,Session��,Session��ռ��,���ʴ���,���ʴ���ռ��,���ʴ���С�ڵ���2��Session��,���ʴ���С�ڵ���2��Session��ռ��', 'left', sql, 700)

mail_end()

sendEmail(['zhongkai.zhao@dianping.com'], [], [], "�ƶ�API�±�", g.HTML_TEXT)
