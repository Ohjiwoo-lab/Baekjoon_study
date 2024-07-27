-- 코드를 입력하세요
SELECT f.FLAVOR
from FIRST_HALF as f, ICECREAM_INFO as i
where f.FLAVOR=i.FLAVOR
AND f.TOTAL_ORDER>3000
AND i.INGREDIENT_TYPE='fruit_based'
order by f.TOTAL_ORDER desc;