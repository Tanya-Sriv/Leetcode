class Solution {
public:
    int reverse(int x) {
        int coeff = 1;
        long n = 0;
        if((x<0)&& (x> ((-1)*pow(2,31)))){
            coeff = (-1);
            n = x *(-1);
        }
        else if ((x>0)&& (x<(pow(2,31)-1))){
            n = x;
        }
        else
           {return 0;}
           
        long int num =0;
        unsigned int r = 0;
        while(n/10 >= 0){
            r = n%10;
            if(n/10 == 0){
                num= (n%10) + num*10;
                break;}
            else{
                num = num*10 + r;
                n = int(n/10);
            }
        } ;
    
        num = num * coeff ; 
        if ((num> (pow(2,31)-1)) || (num < ((-1)*pow(2,31)))){
            return 0;
        }
        else
        return num;
    }
};