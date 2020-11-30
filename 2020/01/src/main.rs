use std::fs;
use std::collections::HashSet;

fn main() {
    let contents = fs::read_to_string("./data/part1.txt").expect("Failed to open file");
    let nums: Vec<i32> = contents.split("\n")
        .filter(|string| !string.is_empty())
        .map(|string| string.parse::<i32>()
        .unwrap())
        .collect();
    
    let part1 = part1(nums);
    println!("{}", part1);
    // 485739
}

fn part1(nums: Vec<i32>) -> i32 {
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
