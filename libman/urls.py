from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('book/', views.view_books, name='view_books'),
    path('book/sortbname', views.order_book_bname, name='order_book_bname'),
    path('book/sortaname', views.order_book_aname, name='order_book_aname'),
    path('book/sortnobooks', views.order_book_nobooks, name='order_book_nobooks'),
    path('book/sortdept', views.order_book_dept, name='order_book_dept'),
    path('book/add/', views.add_book, name='add_book'),
    path('student/', views.view_student, name='view_student'),
    path('student/add/', views.add_student, name='add_student'),
    path('faculty/', views.view_fac, name='view_faculty'),
    path('faculty/add/', views.add_fac, name='add_faculty'),
    path('student/sortfacId', views.order_faculty_facId,
         name='order_faculty_facId'),
    path('student/sortfacname', views.order_faculty_facFname,
         name='order_faculty_facFname'),
    
    path('issue/', views.view_issue, name='view_issue'),
    path('issue/sortisbn', views.order_issue_isbn, name='order_issue_isbn'),
    path('issue/sortbname', views.order_issue_bname, name='order_issue_bname'),
    path('issue/sortbid', views.order_issue_bid, name='order_issue_bid'),
    path('issue/new/', views.new_issue, name='new_issue'),
    path('student/sortstud', views.order_student_studId,
         name='order_student_studId'),
    path('student/sortfname', views.order_student_fname,
         name='order_student_fname'),
    path('student/sortbatch', views.order_student_batch,
         name='order_student_batch'),
    path('student/sortsem', views.order_student_sem, name='order_student_sem'),
    path('student/sortdept', views.order_student_dept, name='order_student_dept'),
    path('return_book/', views.return_book, name='return_book'),

]
