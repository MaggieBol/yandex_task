import pprint
import allpairspy


distance_values = [1, 5, 25]
fragile_values = [True, False]
occupation_values = ["high", "medium", "low"]
size_values = ["large", "small"]


def data_set_by_3():
    result = allpairspy.AllPairs(
        [distance_values, fragile_values, occupation_values, size_values], n=2
    )
    pprint.pprint(list(result))


if __name__ == "__main__":
    print("Generate pairwise data set for next parameters")
    print(f"Distance: {distance_values}")
    print(f"Occupations: {occupation_values}")
    print(f"Size: {size_values}")
    print(f"Fragile: {fragile_values}")
    print("=" * 20)
    data_set_by_3()
    print("=" * 20)