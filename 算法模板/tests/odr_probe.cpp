#include "basic/fast_power.hpp"
#include "dp/lis.hpp"
#include "math/combination.hpp"
#include "string/kmp.hpp"

int odr_probe() {
    return static_cast<int>(fast_power(2, 3, 100) + combination(4, 1));
}
