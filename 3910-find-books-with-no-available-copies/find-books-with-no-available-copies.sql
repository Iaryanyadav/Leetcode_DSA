# Write your MySQL query statement below
with total as (
    select book_id, count(book_id) as counts
    from borrowing_records
    where return_date is NULL
    group by book_id
)
select l.book_id, l.title, l.author, l.genre, l.publication_year, l.total_copies as current_borrowers
from library_books as l
inner join total as t
on l.book_id = t.book_id
where l.total_copies = t.counts
order by l.total_copies desc, l.title asc;