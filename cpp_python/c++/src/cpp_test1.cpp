#include <iostream>
using namespace std;
template <typename T>
struct is_void
{
    static const bool value = false;
};

template <>
struct is_void<void>
{
    static const bool value = true;
};

int main()
{
    std::cout << is_void<int>::value << endl;

    std::cout << is_void<void>::value << endl;
    return 0;
}
  
