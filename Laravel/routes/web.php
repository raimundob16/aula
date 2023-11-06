<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\Controller;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "web" middleware group. Make something great!
|
*/

Route::get('/', [Controller::class,'criarendereco'] )->name('index'); 
Route::post('criar/endereco',[Controller::class,'criar'])->name('criar');
Route::get('listar', [Controller::class,'lista'] )->name('lista');
Route::get('editar/{id}', [Controller::class,'editar'] )->name('editar'); 
Route::post('update/{id}', [Controller::class,'update'] )->name('update'); 
Route::get('deletar/{id}', [Controller::class,'deletar'] )->name('deletar');