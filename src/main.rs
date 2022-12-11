use anyhow::{Context, Result};
use std::{collections::HashMap, fs};

fn main() {
    if let Err(e) = run() {
        panic!("{}", e);
    }
}

fn run() -> Result<()> {
    let input = fs::read_to_string("../5/input.txt")?;
    let lines = input.split('\n');
    let mut stacks: HashMap<usize, Vec<char>> = HashMap::new();

    for line in lines {
        if !line.is_empty() && !line.starts_with("move") && !line.starts_with(" 1") {
            for i in (1..line.len()).step_by(4) {
                let stack_index = (i / 4) + 1;
                // requires ascii
                let nth_char = line.as_bytes()[i] as char;

                match stacks.get_mut(&stack_index) {
                    Some(v) => {
                        if !nth_char.is_whitespace() {
                            v.push(nth_char);
                        }
                    }
                    None => {
                        if !nth_char.is_whitespace() {
                            stacks.insert(stack_index, vec![nth_char]);
                        }
                    }
                };
            }
        }
        if line.starts_with(" 1") {
            for (_k, v) in stacks.iter_mut() {
                v.reverse();
            }
        }

        if line.starts_with("move") {
            let words: Vec<&str> = line.split(" ").collect();

            let mut how_many_to_move = words[1]
                .parse::<usize>()
                .with_context(|| format!("words 1 {:?}", words))?;
            let origin_stack_number = words[3]
                .parse::<usize>()
                .with_context(|| format!("words 3 {}", words[3]))?;
            let dest_stack_number = words[5]
                .parse::<usize>()
                .with_context(|| format!("words 5 {}", words[5]))?;

            while how_many_to_move > 0 {
                let origin_stack = stacks.get_mut(&origin_stack_number).expect("it's in there");
                let the_crate = origin_stack.pop().expect("stacks are nonempty");
                let destination_stack = stacks
                    .get_mut(&dest_stack_number)
                    .expect("It's in there I promise");
                destination_stack.push(the_crate);

                how_many_to_move -= 1;
            }
        }
    }

    let mut res = vec![];
    for i in 1..stacks.len() + 1 {
        let c = stacks.get(&i).unwrap().last().unwrap().clone();
        res.push(c);
    }

    dbg!(&res);

    Ok(())
}
