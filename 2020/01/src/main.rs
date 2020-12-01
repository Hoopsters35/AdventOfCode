use std::fs;
use std::collections::HashSet;

fn main() {
    let contents = fs::read_to_string("./data/part1.txt").expect("Failed to open file");
    let nums: Vec<i32> = contents.split("\n")
        .filter(|string| !string.is_empty())
        .map(|string| string.parse::<i32>()
        .unwrap())
        .collect();
    
    let part1 = part1(&nums);
    println!("{}", part1);
    // 485739

    let part2 = part2(&nums);
    println!("{}", part2);
    // 161109702
}

fn part1(nums: &Vec<i32>) -> i32 {
    let mut targets: HashSet<i32> = HashSet::new();
    for num in nums {
        if targets.contains(&num) {
            return num * (2020 - num);
        } else {
            targets.insert(2020 - num);
        }
    }
    return -1;
}

fn part2(nums: &Vec<i32>) -> i32 {
    let single_vals: HashSet<i32> = nums.iter().cloned().collect();
    for first_val in &single_vals {
        let target = 2020 - first_val;
        let mut targets: HashSet<i32> = HashSet::new();
        for second_val in &single_vals {
            if targets.contains(&second_val) {
                return first_val * second_val * (2020 - first_val - second_val);
            } else {
                targets.insert(target - second_val);
            }
        }
    }
    return -1;
}
