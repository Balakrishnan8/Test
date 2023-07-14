// PROBLEM 50 (MEDIUM) POW(X,N)

public class Powfun
{
  public double power(double base, int n)
  {
    long num = n;
    double ans = 1.0;
    if(n<0)
    {
      num = -1*num;
    }
    while(num>0)
    {
      if(num%2 == 0)
      {
        base *= base;
        num /= 2;
      }
      else
      {
        ans *= base;
        num -= 1;
      }
    }
    if (n<0)
      return (double)1.0/(double)ans;
    return (double)ans;
  }
  public static void main(String[] args)
  {
    Powfun p = new Powfun();
    System.out.println(p.power(2,14));
  }
}