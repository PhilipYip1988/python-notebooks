import sys
other_keys = []
for key in sys.modules:
    if key not in sys.builtin_module_names and not key.startswith('_'):
        other_keys.append(key)

print(f'len: {len(other_keys)}')
print(other_keys)
