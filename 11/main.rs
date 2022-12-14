use num_bigint::BigUint;
use rayon::prelude::*;
use std::{cell::RefCell, vec};

fn main() {
    let mut monkeys = vec![
        Monkey::new(
            vec![
                92usize, 73usize, 86usize, 83usize, 65usize, 51usize, 55usize, 93usize,
            ]
            .into_iter()
            .map(|n| BigUint::from(n))
            .collect(),
            (Operation::Mult, 5),
            (11, 3, 4),
        ),
        Monkey::new(
            vec![99usize, 67usize, 62usize, 61usize, 59usize, 98usize]
                .into_iter()
                .map(BigUint::from)
                .collect(),
            (Operation::Square, 2),
            (2, 6, 7),
        ),
        Monkey::new(
            vec![81usize, 89usize, 56usize, 61usize, 99usize]
                .into_iter()
                .map(BigUint::from)
                .collect(),
            (Operation::Mult, 7),
            (5, 1, 5),
        ),
        Monkey::new(
            vec![97usize, 74usize, 68usize]
                .into_iter()
                .map(BigUint::from)
                .collect(),
            (Operation::Add, 1),
            (17, 2, 5),
        ),
        Monkey::new(
            vec![78usize, 73usize]
                .into_iter()
                .map(BigUint::from)
                .collect(),
            (Operation::Add, 3),
            (19, 2, 3),
        ),
        Monkey::new(
            vec![50usize].into_iter().map(BigUint::from).collect(),
            (Operation::Add, 5),
            (7, 1, 6),
        ),
        Monkey::new(
            vec![95usize, 88usize, 53usize, 75usize]
                .into_iter()
                .map(BigUint::from)
                .collect(),
            (Operation::Add, 8),
            (3, 0, 7),
        ),
        Monkey::new(
            vec![
                50usize, 77usize, 98usize, 85usize, 94usize, 56usize, 89usize,
            ]
            .into_iter()
            .map(BigUint::from)
            .collect(),
            (Operation::Add, 2),
            (13, 4, 0),
        ),
    ];

    for round in 1..10_001 {
        println!("Executing round {}", round);

        for i in 0..monkeys.len() {
            let monkey = monkeys.get_mut(i).unwrap();
            monkey.inspect();
            // monkey.relief();
            let throwns = monkey.throw();
            for (n, dest) in throwns {
                monkeys[dest].catch(n);
            }
        }
    }

    let mut inspections: Vec<usize> = monkeys.iter().map(|m| m.inspected).collect();
    inspections.sort();
    inspections.reverse();

    dbg!(&inspections);

    let sln = inspections[0] * inspections[1];

    println!("{}", sln);
}

enum Operation {
    Add,
    Square,
    Mult,
}

struct Monkey {
    items: RefCell<Vec<BigUint>>,
    operation: (Operation, u32),
    test: (usize, usize, usize),
    inspected: usize,
}

impl Monkey {
    fn new(items: Vec<BigUint>, operation: (Operation, u32), test: (usize, usize, usize)) -> Self {
        Monkey {
            items: RefCell::from(items),
            operation,
            test,
            inspected: 0,
        }
    }

    fn inspect(&mut self) {
        let items = self.items.replace(Vec::new());
        let new: Vec<BigUint> = items
            .into_par_iter()
            .map(|v| Self::perform_operation(&self.operation, &v))
            .collect();

        self.inspected += new.len();
        self.items.replace(new);
    }

    fn relief(&mut self) {
        let items = self.items.replace(Vec::new());
        let new: Vec<BigUint> = items.par_iter().map(|n| n / 3usize).collect();
        self.items.replace(new);
    }

    fn throw(&mut self) -> Vec<(BigUint, usize)> {
        let items = self.items.replace(Vec::new());

        items
            .into_par_iter()
            .map(|v| Self::perform_test(self.test, v))
            .collect()
    }

    fn catch(&mut self, n: BigUint) {
        self.items.borrow_mut().push(n);
    }

    fn perform_operation((operation, n): &(Operation, u32), v: &BigUint) -> BigUint {
        match operation {
            Operation::Add => v + n,
            Operation::Square => v.pow(*n),
            Operation::Mult => n * v,
        }
    }

    fn perform_test(
        (divisor, t_dest, f_dest): (usize, usize, usize),
        v: BigUint,
    ) -> (BigUint, usize) {
        if &v % divisor == BigUint::from(0usize) {
            (v, t_dest)
        } else {
            (v, f_dest)
        }
    }
}
