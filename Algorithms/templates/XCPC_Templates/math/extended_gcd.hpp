#pragma once

#include <optional>
#include <stdexcept>

struct ExtendedGcdResult {
    long long gcd;
    long long x;
    long long y;
};

/** @brief 返回 gcd >= 0 且 a*x + b*y = gcd。 */
inline ExtendedGcdResult extended_gcd(long long a, long long b) {
    long long old_r = a;
    long long r = b;
    long long old_x = 1;
    long long x = 0;
    long long old_y = 0;
    long long y = 1;
    while (r != 0) {
        const long long quotient = old_r / r;
        const long long next_r = old_r - quotient * r;
        old_r = r;
        r = next_r;
        const long long next_x = old_x - quotient * x;
        old_x = x;
        x = next_x;
        const long long next_y = old_y - quotient * y;
        old_y = y;
        y = next_y;
    }
    if (old_r < 0) {
        old_r = -old_r;
        old_x = -old_x;
        old_y = -old_y;
    }
    return {old_r, old_x, old_y};
}

/** @brief 任意正模数下的逆元；不存在时返回 nullopt。 */
inline std::optional<long long> modular_inverse(long long value,
                                                long long modulus) {
    if (modulus <= 0) {
        throw std::invalid_argument("modular_inverse: modulus must be positive");
    }
    const auto result = extended_gcd(value, modulus);
    if (result.gcd != 1) {
        return std::nullopt;
    }
    long long inverse = result.x % modulus;
    if (inverse < 0) {
        inverse += modulus;
    }
    return inverse;
}
