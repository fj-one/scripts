C THIS IS A COMMENT

* THAT WAS A BLANK LINE.
      PROGRAM HELLO  ! INLINE, NO QUOTES
      IMPLICIT NONE  ! INLINE, WITH 'QUOTES'
      REAL A  ! INLINE WITH ONE'QUOTE
      REAL B  ! SAME THING WITH ONE"DOUBLE QUOTE
      REAL C  ! SAME THING WITH TWO"DOUBLE"QUOTES
      A = 1.0
     !  + 2.0        ! EXCLAMATION MARK CAN BE CONTINUATION CHARACTER
      B = 3.0
     C  + 4.0
      C = 5.0
     *  + 6.0
      PRINT *, A
      PRINT *, B
      PRINT *, C
      PRINT *, 'ESCAPE A''INT POSSIBLE!'
      PRINT *, "ESCAPE A""INT POSSIBLE!"
      PRINT *, "ESCAPE A\'INT POSSIBLE!"
      PRINT *, 'ESCAPE A\"INT POSSIBLE!'
      PRINT *, 'ESCAPE A''INT POSSIBLE!'  ! commented
      PRINT *, "ESCAPE A""INT POSSIBLE!"  ! commented
      PRINT *, "ESCAPE A\'INT POSSIBLE!"  ! commented
      PRINT *, 'ESCAPE A\"INT POSSIBLE!'  ! commented
      PRINT *, "ESCAPE A'INT POSSIBLE!"
      PRINT *, 'ESCAPE A"INT POSSIBLE!'
      PRINT *, "ESCAPE A'INT POSSIBLE!"  ! commented
      PRINT *, 'ESCAPE A"INT POSSIBLE!'  ! commented
      PRINT *, 'ESCAPE A"INT POSSIBLE!'  ! so ! many ! comments
      PRINT *, 'ESCAPE A"INT POSSIBLE!'  ! an'd ! wit"h ! 'quotes'
      END PROGRAM HELLO

c     comment at the end; also switched to lower case