program example
    implicit none
    real z
    REAL Z2
    real :: v,x
    real :: a = 3, b=2E12, c = 0.01
    integer :: i, j, k=1, m
    real, parameter :: PI = 3.1415926535897931
    logical :: y = .TRUE. , n = .FALSE.
    complex :: w = (0,1)
    character (len=3) :: month
    real :: array(6)
    real, dimension(4) :: arrayb
    integer :: arrayc(-10:10)
    real :: array2d(3,2)
    real, pointer :: p
    integer, parameter :: LP = selected_real_kind(20)
    real (kind = LP) :: d
    character :: a_char = 'i'
    character (len = 6) :: a_str = "qwerty"
    character (len = 30) :: str_b
    character (len = *), parameter :: a_long_str = "This is a long string."
    str_b = a_str // " keyboard"
    Z = 1
    j = 10 + 2 - 3
    a = 11.54  /  (2.3 * 3.1)
    b = 2**3
    if (z == a) b = 4
    if (z /= a) then
      b = 4
    else if (z .GT. a) then
      b = 6
    else if (z < a) then
      b = 5
    else
      b = 10
    end if
    if (.NOT. (x < c .AND. v >= a .OR. z == z)) then
      inner: if (.TRUE.) then
        b = 1
      endif inner
    endif
    i = 20
    select case (i)
      case (0)
        j=0
      case (1:10)
        j=1
      case (11:)
        j=2
      case default
        j=3
    end select
    month = 'jan'
    monthly: select case (month)
      case ("jan")
         j = 0
      case default
         j = -1
    end select monthly
    do i=2,10,2
      innerloop: do j=1,3
        exit
      end do innerloop
    cycle
    enddo
    goto 10
    stop 1
10  j = 201
    array = (/1,2,3,4,5,6/)
    array = [1,2,3,4,5,6]
    arrayb = [10.2,3e3,0.41,4e-5]
    array2d =  reshape([1.0,2.0,3.0,4.0,5.0,6.0], [3,2])
    v = array(1)
    v = array2d(2,2)
    print *, array(3:5)
    print *, array2d(1,:)
    array = array*3 + 2
    array = array*array
    c = dot_product(array,array)
    c = sum(array)
    c = maxval(array)
    print *, minloc(array)
    c = size(array)
    print *, shape(array)
    m = count(array > 0)
    v = 1
    do i = 1, size(array)
        v = v*array(i)
    end do
    array = [1,2,3,4,5,6]
    where (array > 3)
        array = array + 1
    elsewhere (array == 2)
        array = 1
    elsewhere
        array = 0
    end where
    array = [ (i, i = 1,6) ]
    array = [ (i, i = 1,12,2) ]
    array = [ (i**2, i = 1,6) ]
    array = [ (4,5, i = 1,3) ]
    print *, b
    print "(I6)", 320
    print "(I6.4)", 3
    print "(F6.3)", 4.32
    print "(I3)", 3200
    print "(I5,F6.2,E6.2)", 120, 43.41, 43.41
    print "(3I5)", 10, 20, 30
    print "(2(I5,F6.2))", 120, 43.42, 340, 65.3
    read *, v
    read "(2F6.2)", v, x
    open(unit=11, file="records.txt", status="old")
    read(unit=11, fmt="(3F10.2)") a, b, c
    close(11)
    open(unit=12, file="records.txt", status="replace")
    write(12, "(F10.2,F10.2,F10.2)") c, b, a
    close(12)
    call cpu_time(v)
    k = ior(i,j)
    v = log10(x)
    i = floor(b)
    v = aimag(w)
    call routine(a,c,v)
    m = func(3,2,k)
    Print *, func2(3,2,k)
    m = func3(3,2,k)
contains
    integer function func(a,b,c)
        implicit none
        integer :: a,b,c
        if (a >= 2) then
            func = a + b + c
            return
        endif
        func = a + c
    end function func
    function func2(a,b,c) result(f)
        implicit none
        integer, intent(in) :: a,b
        integer, intent(inout) :: c
        integer :: f
        integer :: cnt = 0
        f = a + b - c
        c = 4
        cnt  = cnt + 1
    end function func2
    pure function func3(a,b,c)
        implicit none
        integer, intent(in) :: a,b,c
        integer :: func3
        func3 = a*b*c
    end function func3
    subroutine routine(d,e,f)
        implicit none
        real, intent(inout) :: f
        real, intent(in) :: d,e
        f = 2*d + 3*e + f
    end subroutine routine
end program example
elemental real function func4(a) result(res)
    real, intent(in) :: a
    res = a**2 + 1.0
end function func4
module fruit
    real :: apple
    real :: pear
    real :: orange
end module fruit
module fruity
    use fruit, only: apple, pear
    implicit none
    private
    public :: apple,mycar,create_mycar
    private :: func4
    interface
        elemental real function func4(a) result(res)
            real, intent(in) :: a
        end function func4
    end interface
    interface myabs
        module procedure real_abs, complex_abs
    end interface
    type car
        character (len=100) :: model
        real :: weight
        real :: dimensions(3)
        character :: colour
    end type car
    type(car) :: mycar
contains
    subroutine create_mycar(mycar)
        implicit none
        type(car),intent(out) :: mycar
        mycar%model = "Ford Prefect"
        mycar%colour = 'r'
        mycar%weight = 1400
        mycar%dimensions(1) = 5.0
        mycar%dimensions(2) = 3.0
        mycar%dimensions(3) = 1.5
    end subroutine
    real function real_abs(x)
        real :: x
        if (x<0) then
            real_abs = -x
        else
            real_abs = x
        end if
    end function real_abs
    real function complex_abs(z)
        complex :: z
        complex_abs = sqrt(real(z)**2 + &
                                         aimag(z)**2)
    end function complex_abs
end module fruity
