.data:
    num prev1 0
    num prev2 1
    num temp 0
    num ost 0
    num max 4000000
    num sum 0

.text:

next: mov 0 temp
      add prev1 temp
      add prev2 temp
      mov prev2 prev1
      mov temp prev2
      cmp prev2 3524578
      je end
      rdiv prev2 2
      sv ost
      cmp ost 0
      je addtosum
      jmp next

addtosum: add prev2 sum
          jmp next

end: add prev2 sum
     out sum
     hlt


