from django.db import models
from django.core.validators import MaxValueValidator, validate_email, ValidationError
import datetime

class Books(models.Model):
    DEPARTMENT = (
        ('CSE', 'Computer Science'),
        ('ISE', 'Information Science'),
        ('ECE', 'Electronics & Communication'),
        ('CIV', 'Civil'),
        ('MECH', 'Mechanical'),
        ('EEE', 'Electrical & Electronics'),
        ('MBA', 'Master in Business Administration'),
    )
    book_id = models.CharField(max_length=20)
    isbn_no = models.CharField(max_length=20, blank=True)
    book_name = models.CharField(max_length=200)
    author_name = models.CharField(max_length=100)
    no_of_books = models.IntegerField()
    department = models.CharField(max_length=3, choices=DEPARTMENT)
    publisher = models.CharField(max_length=100)

    #Trigger
    def Claimbook(self):
        if self.no_of_books > 1:
            self.no_of_books = self.no_of_books-1
            self.save()
        else:
            print("not enough books to Claim")

    def Addbook(self):
        self.no_of_books = self.no_of_books+1
        self.save()

    def __str__(self):
        return self.book_name

    class Meta:
        verbose_name_plural = "Books"



class BORROWER(models.Model):
    Fname = models.CharField(max_length=200)
    Lname = models.CharField(max_length=200)
    Address = models.CharField(max_length=200)
    phone = models.PositiveIntegerField(primary_key=True, validators=[
                                        MaxValueValidator(9999999999)])
    email = models.EmailField(
        max_length=70, blank=True, null=True, unique=True)

    def __str__(self):
        return self.Fname + " " + self.Lname


class Student(BORROWER):
    now = datetime.datetime.now()
    BATCH = [(str(a), str(a)) for a in range(now.year-4, now.year+1)]
    DEPART = (
        ('CSE', 'Computer Science'),
        ('ISE', 'Information Science'),
        ('ECE', 'Electronics & Communication'),
        ('CIV', 'Civil'),
        ('MECH', 'Mechanical'),
        ('EEE', 'Electrical & Electronics'),
        ('MBA', 'Master in Business Administration'),
    )
    student_id = models.CharField(max_length=20, unique=True)
    batch = models.CharField(max_length=4, choices=BATCH)
    depart = models.CharField(max_length=3, choices=DEPART)
    semester = models.CharField(max_length=1)

    def __str__(self):
        return self.Fname+" "+self.Lname


class Faculty(BORROWER):
    fac_id = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.Fname + " " + self.Lname

    class Meta:
        verbose_name_plural = "Faculties"


class Issue(models.Model):
    borrower_id = models.CharField(max_length=20)
    borrower_name = models.CharField(max_length=100)
    book_name = models.CharField(max_length=200)
    book_id = models.CharField(max_length=20)
    issue_date = models.DateField(default=datetime.date.today)
    issue_id = models.CharField(max_length=20)
    isbn = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.book_name


class Return(models.Model):
    return_id = models.CharField(max_length=20)
    return_date = models.DateField(default=datetime.date.today)
    borrower_id = models.CharField(max_length=20)
    borrower_name = models.CharField(max_length=100)
    book_id = models.CharField(max_length=20)
    book_name = models.CharField(max_length=200)
    isbn_no = models.CharField(max_length=20)

    def __str__(self):
        return self.book_name


class Semester(models.Model):
    SEM = (
        ('1', 'first'),
        ('2', 'second'),
        ('3', 'third'),
        ('4', 'fourth'),
        ('5', 'fifth'),
        ('6', 'sixth'),
        ('7', 'seventh'),
        ('8', 'eighth')
    )
    DEPART = (
        ('CSE', 'Computer Science'),
        ('ISE', 'Information Science'),
        ('ECE', 'Electronics & Communication'),
        ('CIV', 'Civil'),
        ('MECH', 'Mechanical'),
        ('EEE', 'Electrical & Electronics'),
        ('MBA', 'Master in Business Administration'),
    )
    sem = models.CharField(max_length=1)
    depart = models.CharField(max_length=3)
    subject = models.CharField(max_length=30)

    def __str__(self):
        return depart + ' ' + sem
