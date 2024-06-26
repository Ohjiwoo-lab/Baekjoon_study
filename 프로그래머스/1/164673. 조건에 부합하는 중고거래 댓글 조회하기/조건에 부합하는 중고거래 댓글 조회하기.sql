-- 코드를 입력하세요
SELECT b.title, b.board_id, r.reply_id, r.writer_id, r.contents, DATE_FORMAT(r.created_date, "%Y-%m-%d") as create_date
from used_goods_board as b, used_goods_reply as r
where b.board_id=r.board_id and DATE_FORMAT(b.created_date, "%Y%m")="202210"
order by r.created_date, b.title;