use std::fs;
use std::collections::HashSet;

fn main() {
    let contents = fs::read_to_string("./data/part1.txt").expect("Failed to open file");
    let nums: Vec<i32> = contents.split("\n")
        .filter(|string| !string.is_empty())
        .map(|string| string.parse::<i32>().unwrap())
        .collect();

    let part1 = part1(&nums);
    println!("{}", part1);
    // 485739

    let part2 = part2(&nums);
    println!("{}", part2);
    // 161109702
}

fn index_removed(list: &[i32], i: usize) -> Vec<i32> {
    let l1 = &list[..i];
    let l2 = &list[i+1..];
    return [l1, l2].concat();
}

fn find_pair(nums: &Vec<i32>, target: i32) -> (i32, i32) {
    let mut targets: HashSet<i32> = HashSet::new();
    for num in nums {
        if targets.contains(&num) {
            return (*num, (target - num));
        } else {
            targets.insert(target - num);
        }
    }
    return (-1, -1);
}

fn part1(nums: &Vec<i32>) -> i32 {
    let (num1, num2) = find_pair(&nums, 2020);
    return num1 * num2;
}

fn part2(nums: &Vec<i32>) -> i32 {
    for (i, first_val) in nums.iter().enumerate() {
        let target = 2020 - first_val;
        let remainin_vals = index_removed(&nums, i);
        let (second_val, third_val) = find_pair(&remainin_vals, target);
        if second_val != -1 {
            return second_val * third_val * first_val;
        }
    }
    return -1;
}
