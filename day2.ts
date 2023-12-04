const fs = require('fs');

type Game = {
    id: number;
    rounds: Round[];
}

type Round = Record<string, number>;


function getInput(): string[] {
    const content = fs.readFileSync('day2_input.txt', { encoding: 'utf-8' });
    return content.split('\n').filter((e: unknown) => !!e);
    // return [
    //     'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
    //     'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
    //     'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
    //     'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
    //     'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green',
    // ];
}

function parseGame(line: string): Game {
    let [gamestr, roundStr] = line.split(':');
    let gameNo = gamestr.match(/(\d+)/)?.[1]!;

    let roundstrings = roundStr.split(';');

    let rounds: Round[] = [];

    for (let roundstr of roundstrings) {
        let results = roundstr.matchAll(/(\d+) ([a-z]+)/ig)

        let round: Round = {};
        for (let match of results) {
            round[match[2]] = Number.parseInt(match[1]);
        }

        rounds.push(round);
    }
    
    let game: Game = {
        id: Number.parseInt(gameNo),
        rounds: rounds,
    };
    return game;
}

function is_game_possible(game: Game): boolean {
    return game.rounds.every(r => getFromRecord(r, 'blue') <= 14 && getFromRecord(r, 'green') <= 13 && getFromRecord(r, 'red') <= 12);
}

function getFromRecord(dict: Record<string, number>, val: string) {
    return dict[val] || 0;
}

function main() {
    let input = getInput();

    let sum = 0;

    for (let gamestr of input) {
        let game = parseGame(gamestr)
        
        if (is_game_possible(game)) {
            sum += game.id;
            console.log(game.id, 'possible');
        }
    }
    
    console.log(sum);
}

main();