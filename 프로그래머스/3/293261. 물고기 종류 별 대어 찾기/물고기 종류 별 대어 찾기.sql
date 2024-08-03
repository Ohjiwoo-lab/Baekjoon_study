-- 코드를 작성해주세요
select ID, n.FISH_NAME, LENGTH
from FISH_INFO as one, FISH_NAME_INFO as n
where LENGTH=(select max(LENGTH)
             from FISH_INFO as two
             where two.FISH_TYPE=one.FISH_TYPE)
and one.FISH_TYPE=n.FISH_TYPE
order by ID;