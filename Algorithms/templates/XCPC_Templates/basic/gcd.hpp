#pragma once

#include <numeric>
#include <limits>
#include <stdexcept>

/** @brief 最大公约数，结果非负。 */
inline long long gcd(long long a, long long b) {
    return std::gcd(a, b);
}

/**
 * @brief 最小公倍数；任一参数为 0 时返回 0。
 * @throws std::overflow_error 当结果超出 long long。
 */
inline long long lcm(long long a, long long b) {
    if (a == 0 || b == 0) {
        return 0;
    }
    const __int128 value = static_cast<__int128>(a / gcd(a, b)) * b;
    const __int128 absolute = value < 0 ? -value : value;
    if (absolute > static_cast<__int128>(
                       std::numeric_limits<long long>::max())) {
        throw std::overflow_error("lcm: result does not fit in long long");
    }
    return static_cast<long long>(absolute);
}
