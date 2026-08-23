#pragma once

#include <stdexcept>

namespace modular {
inline constexpr long long MOD = 1'000'000'007LL;

inline long long normalize(long long value) {
    value %= MOD;
    return value < 0 ? value + MOD : value;
}

inline long long add(long long left, long long right) {
    return (normalize(left) + normalize(right)) % MOD;
}

inline long long sub(long long left, long long right) {
    return (normalize(left) - normalize(right) + MOD) % MOD;
}

inline long long mul(long long left, long long right) {
    return (normalize(left) * normalize(right)) % MOD;
}

inline long long fast_pow(long long base, long long exponent) {
    if (exponent < 0) {
        throw std::invalid_argument("modular::fast_pow: negative exponent");
    }
    long long result = 1;
    base = normalize(base);
    while (exponent > 0) {
        if ((exponent & 1LL) != 0) {
            result = mul(result, base);
        }
        base = mul(base, base);
        exponent >>= 1;
    }
    return result;
}

/** @note MOD 为素数；a 必须不为 0 (mod MOD)。 */
inline long long inv(long long value) {
    if (normalize(value) == 0) {
        throw std::domain_error("modular::inv: zero has no inverse");
    }
    return fast_pow(value, MOD - 2);
}

inline long long div(long long numerator, long long denominator) {
    return mul(numerator, inv(denominator));
}
}  // namespace modular
