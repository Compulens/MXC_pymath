desired_mean = 15
desired_std = 4.3

# 1. Start with any random distribution (1000 samples)
nums = np.random.randn(1000)

# 2. Force the mean to exactly 0 and std dev to exactly 1 (Z-score normalization)
nums = (nums - np.mean(nums)) / np.std(nums)

# 3. Scale to exact desired std dev and shift to exact desired mean
nums = nums * desired_std + desired_mean

# --- Your plotting code ---
plt.subplot(121)
plt.plot(nums, 's')

plt.subplot(122)
plt.hist(nums)
plt.show()

# --- Verification ---
print(f'Actual Std:  {np.std(nums)}')
print(f'Actual Mean: {np.mean(nums)}')
