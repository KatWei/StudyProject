<?php

use Faker\Generator as Faker;

$factory->define(App\Models\Topic::class, function (Faker $faker) {
    $sentence = $faker->sentence();

    $update_at = $faker->dateTimeThisMonth();

    $created_at = $faker->dateTimeThisMonth($update_at);

    return [
        'title' => $sentence,
        'body' => $faker->text(),
        'excerpt' => $sentence,
        'created_at' => $created_at,
        'updated_at' => $update_at
    ];
});
