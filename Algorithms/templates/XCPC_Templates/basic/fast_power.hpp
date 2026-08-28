#pragma once

#include <stdexcept>

/**
 * @brief 计算 base^exp mod mod。
 * @throws std::invalid_argument 当 exp < 0 或 mod <= 0。
 * @time_complexity O(log exp)
 */
inline long long fast_power(long long base, long long exp, long long mod) {
    if (exp < 0) {
        throw std::invalid_argument("fast_power: exponent must be non-negative");
    }
    if (mod <= 0) {
        throw std::invalid_argument("fast_power: modulus must be positive");
    }
    if (mod == 1) {
        return 0;
    }

    base %= mod;
    if (base < 0) {
        base += mod;
    }

    long long result = 1 % mod;
    while (exp > 0) {
        if ((exp & 1LL) != 0) {
            result = static_cast<long long>(
                (static_cast<__int128>(result) * base) % mod);
        }
        base = static_cast<long long>(
            (static_cast<__int128>(base) * base) % mod);
        exp >>= 1;
    }
    return result;
}
