#include <boost/type_traits.hpp>
#include <cstring>
#include <cstdio>
#include <iostream>
namespace detail
{
    template <bool b>
    struct copier
    {
        template<typename I1, typename I2>
        static I2 do_copy(I1 first, I1 last, I2 out);
    };

    template <bool b>
    template<typename I1, typename I2>
    I2 copier<b>::do_copy(I1 first, I1 last, I2 out)
    {
        while(first != last)
        {
            *out = *first;
            ++out;
            ++first;
        }
        return out;
    }

    template <>
    struct copier<true>
    {
        template<typename I1, typename I2>
        static I2 *do_copy(I1 *first, I1 *last, I2 *out)
        {
            memcpy(out, first, (last - first)*sizeof(I2));
            return out + (last - first);
        }
    };
}

template<typename I1, typename I2>
inline I2 copy(I1 first, I1 last, I2 out)
{
    typedef typename
    boost::remove_cv <typename std::iterator_traits<I1>::value_type >::type v1_t;
    typedef typename
    boost::remove_cv <typename std::iterator_traits<I2>::value_type >::type v2_t;
    enum { can_opt =
               boost::is_same<v1_t, v2_t>::value
           && boost::is_pointer<I1>::value
           && boost::is_pointer<I2>::value
           && boost::
           has_trivial_assign<v1_t>::value
         };
    return detail::copier<can_opt>::
           do_copy(first, last, out);
}

int main(int argc, char const *argv[])
{
    int a[10] = {2};
    int b[10];
    copy<int *, int * >(a, a + 9, b);
    std::cout << b[0] << std::endl;
    return 0;
}