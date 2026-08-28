#pragma once

#include <stdexcept>
#include <vector>

/** @brief 埃拉托斯特尼筛，返回 [0, n] 的素数标记。 */
inline std::vector<bool> eratosthenes_sieve(int n) {
    if (n < 0) {
        throw std::invalid_argument("eratosthenes_sieve: n must be non-negative");
    }
    std::vector<bool> is_prime(static_cast<std::size_t>(n) + 1, true);
    is_prime[0] = false;
    if (n < 2) {
        return is_prime;
    }
    is_prime[1] = false;
    for (int i = 2; i <= n / i; ++i) {
        if (!is_prime[i]) {
            continue;
        }
        for (int j = i * i; j <= n; j += i) {
            is_prime[j] = false;
        }
    }
    return is_prime;
}

/** @brief 线性筛，返回不大于 n 的所有素数。 */
inline std::vector<int> linear_sieve(int n) {
    if (n < 0) {
        throw std::invalid_argument("linear_sieve: n must be non-negative");
    }
    std::vector<bool> composite(static_cast<std::size_t>(n) + 1, false);
    std::vector<int> primes;
    for (int i = 2; i <= n; ++i) {
        if (!composite[i]) {
            primes.push_back(i);
        }
        for (int prime : primes) {
            if (prime > n / i) {
                break;
            }
            composite[i * prime] = true;
            if (i % prime == 0) {
                break;
            }
        }
    }
    return primes;
}
