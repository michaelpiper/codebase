<?php
    class PyramindCoinChange{
        private $coins=array();
        private $num_coin_types=0;
        public function __construct($coin_types){
            // save the coin types in coins
            // add pyramid form to coins
            rsort($coin_types);
            $this->coins=$coin_types;
            $this->num_coin_types=count($coin_types);
        }
        // pass amount to this function
        public function generate_coins($amount){
             $final_result=[];
             $total_amount=$amount;
            // loop through the coin types. for each type find how many 
            // of the amount you can get
             for ($i = 0; $i < $this->num_coin_types; $i++) {
                // first get the value of the coin type
                $current_type_value = $this->coins[$i];
                // count the number of that type of coin.
                // by calculating the currentTypeValue over totalAmount
                $type_count = floor($total_amount / $current_type_value);
                // push the coin count into result
                $final_result[]=$type_count;
                // update the total amount so on the next iteration we can find the right
                // type count
                $total_amount -= ($current_type_value * $type_count);
             }
            // return the final results
            return $final_result;
        }
        // display the list of coins generated 
        public function display_results($amount){
            $results = $this->generate_coins($amount);
            print_r($results);
            for($i = 0; $i < count($results); $i++) {
                print('There are( '.$results[$i].' ) '. $this->coins[$i].' Naira'.PHP_EOL);
            }
        }

    }

    $coin_types=[25,10,7,2];
    $coin_changer=new PyramindCoinChange($coin_types);
    $coin_changer->display_results(191);

    // Dynamic Programming is a method for solving a complex problem by breaking it down into a collection of simpler subproblems,
    // solving each of those subproblems just once, and storing their solutions using a memory-based data structure (array, map,etc).

    // A greedy algorithm is a simple, intuitive algorithm that is used in optimization problems.
    // The algorithm makes the optimal choice at each step as it attempts to find the overall optimal way to solve the entire problem.

    // pyramid form is a form
    // in which information is presented in descending order of importance. 
    // This allows the audience to read the most crucial details quickly 
    // so they can decide whether to continue or stop reading the story.

    // before going through the loop i arranged the coins in pyramid form
    // after wards i got the value of the coin type
    // counted the number of that type of coin.
    // by calculating the currentTypeValue over totalAmount
    // push the coin count into result
    // update the total amount so on the next iteration i found the right
    // type count
    // return the final results
    // display the list of coins generated 