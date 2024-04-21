(*1a*)
fun reverse (h::t : int list) = (reverse t) @ [h]
  | reverse [] = [];
 

 
reverse [];
reverse [3, 1, 8, 0];   

(*1b*)
fun reverse (lst: int list)   = 
  let
    fun rev ([]: int list ) temp = temp 
        | rev (x::xs : int list) temp = rev xs (x::temp)
    in
        rev lst []
    end; 
  

reverse [];
reverse [3, 1, 8, 0];
(* 
* CSCI3180 Principles of Programming Languages
*
* --- Declaration ---
* I declare that the assignment here submitted is original except for source
* materials explicitly acknowledged. I also acknowledge that I am aware of
* University policy and regulations on honesty in academic work, and of the
* disciplinary guidelines and procedures applicable to breaches of such policy
* and regulations, as contained in the website
* http://www.cuhk.edu.hk/policy/academichonesty/
*
* Name: Tsang Cheuk Hnag
* Student ID: 1155167650
* Email Address: 1155167650@link.cuhk.edu.hk
*
* Source material acknowledgements (if any):
* 
* Students whom I have discussed with (if any):
*
*)

(*2*)
(* constructers *)
datatype term = Term of int * int * int;
datatype variable = Variable of string;
datatype poly = Poly of variable * variable * term list;

(* For example: 3x^3y + x^2 - 4y^2 + 2xy + 1 *)
(* Poly(Variable "x", Variable "y", [Term(3, 1, 3), Term(2, 0, 1), Term(0, 2, ~4), Term(1, 1, 2), Term(0, 0, 1)]) *)
(* Note that we assume x and y are two variables, and the 1st and 2nd elements of term are the exponentials of x and y, respectively. *)
 
(* Several functions you may find helpful for computations over polynomials *)
fun expon_x (Term(e, _, _)) = e;
fun expon_y (Term(_, e, _)) = e;
fun coeff (Term(_, _, c)) = c;

exception VariableMismatch;

fun diff_terms (l : term list, v : variable) : term list =
  let 
    val x = Variable "x"; 
    val y = Variable "y";
    val head = hd l
    val tail = tl l
    val tail_null = null tail
    val return_data = 
    if  x = v then 
        if expon_x(head) = 0 then
                Term(0,0,0)
        else
            Term(expon_x(head)-1,expon_y(head),expon_x(head)*coeff(head))
    else 
        if expon_y(head) = 0 then
                Term(0,0,0)
        else
        Term(expon_x(head),expon_y(head)-1,expon_y(head)*coeff(head))
  in 
    if tail_null then
      [return_data]
    else
      return_data :: diff_terms(tail, v)
  end;
  
(* Your implementation here *)

fun diff_poly (Poly(xx, yy, l), v) : poly = 
  if (xx = v) orelse (yy = v) then 
    Poly (xx, yy, diff_terms (l, v))
  else
    raise VariableMismatch 
;



val x = Variable "x"; 
val y = Variable "y";

val p = Poly(x, y, [Term(3, 1, 3), Term(2, 0, 1), Term(0, 2, ~4), Term(1, 1, 2), Term(0, 0, 1)]);


diff_poly (p, x);

(*part 2*)
fun max(x,y) = if x > y then x else y

(*2.1*)
fun check_bull(lst: int list): bool =
    let
        fun check _ _ [] = false
          | check x y (z::zs) =
            if (x + y + z) mod 10  = 0 then
                true
            else
                check x y zs

        fun check_j x (y::ys) (z::zs) =
            if check x y (z::zs) = true then
                true
            else
                if length zs = 0 then
                    false
                else
                check_j x ys zs

        fun check_i (x::xs) (y::ys) (z::zs) =
            if check_j x (y::ys) (z::zs) = true then
                true
            else
                if length ys = 0 orelse length zs = 0 then
                    false
                else
                    check_i xs ys zs

        val i_list = lst
        val j_list = tl lst
        val k_list = tl (tl lst)
    in
        check_i i_list j_list k_list
    end;
 
(*2.2*)   
fun get_point_bull(lst: int list): int =
    let

        fun sumList [] = 0
          | sumList (x::xs) = x + sumList xs
      
        val total = sumList lst
      
    in
        if total mod 10 = 0then 
            10
        else 
            total mod 10
    end;


(*2.3*)

fun get_point_non_bull (nil) = 0
  | get_point_non_bull (x::nil) = x
  | get_point_non_bull (x::xs) = let val y = get_point_non_bull (xs) in max(x,y) end;
  
get_point_non_bull  [10, 2, 6, 2, 4];     
get_point_non_bull  [7, 3, 10, 2, 8];


(*2.4*)
fun compare_result(lst1: int list, lst2: int list): string =
    let
        val p1_bull = check_bull(lst1)
        val p2_bull = check_bull(lst2)
        
        val p1_non_bull = get_point_non_bull(lst1)
        val p2_non_bull = get_point_non_bull(lst2)
    in 
        if p1_bull andalso p2_bull then 
            if get_point_bull(lst1) > get_point_bull(lst2) then 
            "Player 1 wins"
            else if get_point_bull(lst1) < get_point_bull(lst2) then 
            "Player 2 wins" 
            else "This is a tie"
            
        else if p1_bull andalso not p2_bull then
            "Player 1 wins"
        else if not p1_bull andalso p2_bull then
            "Player 2 wins"
        else
            if p1_non_bull > p2_non_bull then 
            "Player 1 wins"
            else if p1_non_bull < p2_non_bull then 
            "Player 2 wins"
            else "This is a tie"
    end;
        


check_bull [3,3,3,4,3];     (* return: true *)
check_bull [3, 7, 4, 6, 5];      (* return: false *)
get_point_bull [10, 2, 6, 2, 4]; 
get_point_bull [7, 3, 10, 2, 8];  

val lst1 = [10, 6, 2, 2, 8];
val lst2 = [7, 3, 1, 6, 1];
compare_result (lst1, lst2);  
 