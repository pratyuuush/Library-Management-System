from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import BookForm, StudentForm, FacultyForm, IssueForm, ReturnForm
from .models import Books, Student, Faculty, Issue, Return, Semester
from django.views.generic import UpdateView, DeleteView
from django.db.models import Q


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required(login_url='/login/')
def index(request):
    return render(request, 'libman/home.html')


@login_required(login_url='/login/')
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('view_books')

    else:
        form = BookForm()

    return render(request, 'libman/add_book.html', {'form': form})


@login_required(login_url='/login/')
def view_books(request):
    books = Books.objects.order_by('department')
    query = request.GET.get('q')
    if query:
        books = Books.objects.filter(Q(book_name__icontains=query) | Q(author_name__icontains=query) | Q(
            book_detail__icontains=query) | Q(department__icontains=query))
    else:
        books = Books.objects.order_by('department')
    return render(request, 'libman/view_book.html', {'books': books})


@login_required(login_url='/login/')
def order_student_studId(request):
    students = Student.objects.order_by('student_id')
    query = request.GET.get('q')
    if query:
        students = Student.objects.filter(Q(Fname__icontains=query) | Q(Lname__icontains=query) | Q(
            phone__icontains=query) | Q(depart__icontains=query) | Q(student_id__icontains=query))
    else:
        students = Student.objects.order_by('student_id')
    return render(request, 'libman/view_student.html', {'students': students})


@login_required(login_url='/login/')
def order_student_dept(request):
    students = Student.objects.order_by('depart')
    query = request.GET.get('q')
    if query:
        students = Student.objects.filter(Q(Fname__icontains=query) | Q(Lname__icontains=query) | Q(
            phone__icontains=query) | Q(depart__icontains=query) | Q(student_id__icontains=query))
    else:
        students = Student.objects.order_by('depart')
    return render(request, 'libman/view_student.html', {'students': students})


@login_required(login_url='/login/')
def order_student_sem(request):
    students = Student.objects.order_by('semester')
    query = request.GET.get('q')
    if query:
        students = Student.objects.filter(Q(Fname__icontains=query) | Q(Lname__icontains=query) | Q(
            phone__icontains=query) | Q(depart__icontains=query) | Q(student_id__icontains=query))
    else:
        students = Student.objects.order_by('semester')
    return render(request, 'libman/view_student.html', {'students': students})


@login_required(login_url='/login/')
def order_student_fname(request):
    students = Student.objects.order_by('Fname')
    query = request.GET.get('q')
    if query:
        students = Student.objects.filter(Q(Fname__icontains=query) | Q(Lname__icontains=query) | Q(
            phone__icontains=query) | Q(depart__icontains=query) | Q(student_id__icontains=query))
    else:
        students = Student.objects.order_by('Fname')
    return render(request, 'libman/view_student.html', {'students': students})


@login_required(login_url='/login/')
def order_student_batch(request):
    students = Student.objects.order_by('batch')
    query = request.GET.get('q')
    if query:
        students = Student.objects.filter(Q(Fname__icontains=query) | Q(Lname__icontains=query) | Q(
            phone__icontains=query) | Q(depart__icontains=query) | Q(student_id__icontains=query))
    else:
        students = Student.objects.order_by('batch')
    return render(request, 'libman/view_student.html', {'students': students})


@login_required(login_url='/login/')
def order_book_bname(request):
    books = Books.objects.order_by('book_name')
    query = request.GET.get('q')
    if query:
        books = Books.objects.filter(Q(book_name__icontains=query) | Q(author_name__icontains=query) | Q(
            book_detail__icontains=query) | Q(department__icontains=query))
    else:
        books = Books.objects.order_by('book_name')
    return render(request, 'libman/view_book.html', {'books': books})


@login_required(login_url='/login/')
def order_book_aname(request):
    books = Books.objects.order_by('author_name')
    query = request.GET.get('q')
    if query:
        books = Books.objects.filter(Q(book_name__icontains=query) | Q(author_name__icontains=query) | Q(
            book_detail__icontains=query) | Q(department__icontains=query))
    else:
        books = Books.objects.order_by('author_name')
    return render(request, 'libman/view_book.html', {'books': books})


@login_required(login_url='/login/')
def order_book_nobooks(request):
    books = Books.objects.order_by('no_of_books')
    query = request.GET.get('q')
    if query:
        books = Books.objects.filter(Q(book_name__icontains=query) | Q(author_name__icontains=query) | Q(
            book_detail__icontains=query) | Q(department__icontains=query))
    else:
        books = Books.objects.order_by('no_of_books')
    return render(request, 'libman/view_book.html', {'books': books})


@login_required(login_url='/login/')
def order_book_dept(request):
    books = Books.objects.order_by('department')
    query = request.GET.get('q')
    if query:
        books = Books.objects.filter(Q(book_name__icontains=query) | Q(author_name__icontains=query) | Q(
            book_detail__icontains=query) | Q(department__icontains=query))
    else:
        books = Books.objects.order_by('department')
    return render(request, 'libman/view_book.html', {'books': books})


@login_required(login_url='/login/')
def add_student(request):
    if request.method == 'POST':
        s_form = StudentForm(request.POST)
        if s_form.is_valid():
            s_form.save(commit=True)
            return redirect('view_student')
    else:
        s_form = StudentForm()
    return render(request, 'libman/add_student.html', {'s_form': s_form})


@login_required(login_url='/login/')
def add_fac(request):
    if request.method == 'POST':
        f_form = FacultyForm(request.POST)
        if f_form.is_valid():
            f_form.save(commit=True)
            return redirect('view_faculty')
    else:
        f_form = FacultyForm()
    return render(request, 'libman/add_faculty.html', {'f_form': f_form})


@login_required(login_url='/login/')
def view_fac(request):
    faculties = Faculty.objects.order_by('fac_id')
    query = request.GET.get('q')
    if query:
        faculties = Faculty.objects.filter(Q(Fname__icontains=query) | Q(Lname__icontains=query) | Q(
            phone__icontains=query) | Q(email__icontains=query))
    else:
        faculties = Faculty.objects.order_by('fac_id')
    return render(request, 'libman/view_faculty.html', {'faculties': faculties})


@login_required(login_url='/login/')
def view_student(request):
    students = Student.objects.order_by('batch')
    query = request.GET.get('q')
    if query:
        students = Student.objects.filter(Q(Fname__icontains=query) | Q(Lname__icontains=query) | Q(
            phone__icontains=query) | Q(email__icontains=query))
    else:
        students = Student.objects.order_by('batch')
    return render(request, 'libman/view_student.html', {'students': students})


@login_required(login_url='/login/')
def order_faculty_facId(request):
    faculties = Faculty.objects.order_by('fac_id')
    query = request.GET.get('q')
    if query:
        faculties = Faculty.objects.filter(Q(Fname__icontains=query) | Q(Lname__icontains=query) | Q(
            phone__icontains=query) | Q(email__icontains=query))
    else:
        faculties = Faculty.objects.order_by('fac_id')
    return render(request, 'libman/view_faculty.html', {'faculties': faculties})


@login_required(login_url='/login/')
def order_faculty_facFname(request):
    faculties = Faculty.objects.order_by('Fname')
    query = request.GET.get('q')
    if query:
        faculties = Faculty.objects.filter(Q(Fname__icontains=query) | Q(Lname__icontains=query) | Q(
            phone__icontains=query) | Q(email__icontains=query))
    else:
        faculties = Faculty.objects.order_by('Fname')
    return render(request, 'libman/view_faculty.html', {'faculties': faculties})




@login_required(login_url='/login/')
def view_issue(request):
    issue = Issue.objects.order_by('borrower_name', 'issue_date')
    return render(request, 'libman/view_issue.html', {'issue': issue})


@login_required(login_url='/login/')
def new_issue(request):
    if request.method == 'POST':
        i_form = IssueForm(request.POST)

        if i_form.is_valid():
            name = i_form.cleaned_data['borrower_id']
            book = i_form.cleaned_data['isbn']
            i_form.save(commit=True)
            books = Books.objects.get(isbn_no=book)
            semest = Student.objects.get(student_id=name).semester
            departm = Student.objects.get(student_id=name).depart
            Books.Claimbook(books)
            return redirect('view_issue')
    else:
        i_form = IssueForm()
    semest = None
    departm = None
    sem_book = Semester.objects.filter(sem=semest, depart=departm)
    return render(request, 'libman/new_issue.html', {'i_form': i_form, 'sem_book': sem_book})


@login_required(login_url='/login/')
def order_issue_isbn(request):
    issue = Issue.objects.order_by('isbn')
    query = request.GET.get('q')
    if query:
        issue = Issue.objects.filter(Q(Fname__icontains=query) | Q(Lname__icontains=query) | Q(
            phone__icontains=query) | Q(email__icontains=query))
    else:
        issue = Issue.objects.order_by('isbn')
    return render(request, 'libman/view_issue.html', {'issue': issue})


@login_required(login_url='/login/')
def order_issue_bname(request):
    issue = Issue.objects.order_by('book_name')
    query = request.GET.get('q')
    if query:
        issue = Issue.objects.filter(Q(Fname__icontains=query) | Q(Lname__icontains=query) | Q(
            phone__icontains=query) | Q(email__icontains=query))
    else:
        issue = Issue.objects.order_by('book_name')
    return render(request, 'libman/view_issue.html', {'issue': issue})


@login_required(login_url='/login/')
def order_issue_bid(request):
    issue = Issue.objects.order_by('borrower_id')
    query = request.GET.get('q')
    if query:
        issue = Issue.objects.filter(Q(Fname__icontains=query) | Q(Lname__icontains=query) | Q(
            phone__icontains=query) | Q(email__icontains=query))
    else:
        issue = Issue.objects.order_by('borrower_id')
    return render(request, 'libman/view_issue.html', {'issue': issue})


@login_required(login_url='/login/')
def return_book(request):
    if request.method == 'POST':
        r_form = ReturnForm(request.POST)
        if r_form.is_valid():
            r_form.save(commit=True)
            book = r_form.cleaned_data['isbn_no']
            books = Books.objects.get(isbn_no=book)
            b_id = r_form.cleaned_data['borrower_id']
            Books.Addbook(books)
            Issue.objects.filter(borrower_id=b_id, isbn=book).delete()
            return redirect('view_issue')
    else:
        r_form = ReturnForm()
    return render(request, 'libman/return_book.html', {'r_form': r_form})


def redir(request):
    return redirect('home')
