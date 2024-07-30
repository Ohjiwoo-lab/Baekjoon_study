SELECT i.REST_ID, i.REST_NAME, i.FOOD_TYPE, i.FAVORITES, i.ADDRESS, round(avg(r.REVIEW_SCORE),2) as SCORE
from REST_INFO as i, REST_REVIEW as r
where substring_index(i.ADDRESS, ' ', 1) in ('서울특별시', '서울시')
and i.REST_ID=r.REST_ID
group by i.REST_ID
order by round(avg(r.REVIEW_SCORE),2) desc, i.FAVORITES desc;