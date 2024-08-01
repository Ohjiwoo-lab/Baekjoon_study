-- 코드를 작성해주세요
select ECOLI_DATA2.ID, ECOLI_DATA2.GENOTYPE, ECOLI_DATA2.PARENT_GENOTYPE
from (select 
      a.ID, a.PARENT_ID, a.GENOTYPE, b.GENOTYPE as PARENT_GENOTYPE,
      substring(reverse(convert(conv(a.GENOTYPE,10,2),char)),1,length(convert(conv(b.GENOTYPE,10,2),char))) as one, 
      replace(reverse(convert(conv(b.GENOTYPE,10,2),char)), '0','_') as two
     from ECOLI_DATA as a left join ECOLI_DATA as b on a.PARENT_ID=b.ID) ECOLI_DATA2
where ECOLI_DATA2.one like ECOLI_DATA2.two
order by ECOLI_DATA2.ID;