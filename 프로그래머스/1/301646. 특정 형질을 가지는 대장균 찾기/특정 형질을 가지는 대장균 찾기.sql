-- 코드를 작성해주세요
select count(id) as COUNT
from ECOLI_DATA
where substring(convert(conv(GENOTYPE,10,2),char),-2,1)!=1
and (substring(convert(conv(GENOTYPE,10,2),char),-1,1)=1
     or substring(convert(conv(GENOTYPE,10,2),char),-3,1)=1)