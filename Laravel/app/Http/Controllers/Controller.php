<?php

namespace App\Http\Controllers;

use App\Models\Endereco;
use App\Models\Cliente;
use Illuminate\Foundation\Auth\Access\AuthorizesRequests;
use Illuminate\Foundation\Validation\ValidatesRequests;
use Illuminate\Routing\Controller as BaseController;
use Illuminate\Http\Request;

class Controller extends BaseController
{
    use AuthorizesRequests, ValidatesRequests;

    public function criarendereco(){
        return view("welcome");
    }

    public function criar(Request $request){
        $endereco = new Endereco();
        $endereco->cep = $request->input("cep");
        $endereco->uf = $request->input("uf");
        $endereco->cidade = $request->input("cidade");
        $endereco->barrio = $request->input("barrio");
        $endereco->rua = $request->input("rua");
        $endereco->pais = $request->input("pais");
        $endereco->numero = $request->input("numero");
        $endereco->complemento = $request->input("complemento");
        $endereco->save();

        $cliente = new Cliente();
        $cliente->name = $request->input("nome");
        $cliente->telefone = $request->input("telefone");
        $cliente->email = $request->input("email");
        $cliente->id_endereco = $endereco->id;
        $cliente->save();
    }

    public function update(Request $request,$id){
        $endereco = Endereco::find($id);
        $endereco->cep = $request->input("cep");
        $endereco->uf = $request->input("uf");
        $endereco->cidade = $request->input("cidade");
        $endereco->barrio = $request->input("barrio");
        $endereco->rua = $request->input("rua");
        $endereco->pais = $request->input("pais");
        $endereco->numero = $request->input("numero");
        $endereco->complemento = $request->input("complemento");
        $endereco->update();

        $cliente = Cliente::find($id);
        $cliente->name = $request->input("nome");
        $cliente->telefone = $request->input("telefone");
        $cliente->email = $request->input("email");
        $cliente->id_endereco = $endereco->id;
        $cliente->update();
    }

        public function lista(){
            $cliente = Cliente::select(
            'cliente.id',
            'cliente.name',
            'cliente.telefone',
            'cliente.email',
            'endereco.cep',
            'endereco.uf',
            'endereco.cidade',
            'endereco.barrio',
            'endereco.rua',
            'endereco.numero',
            'endereco.complemento'
            )
            ->join('endereco','endereco.id','=','cliente.id_endereco')
            ->get();
            return view("listar", compact("cliente"));
            
         
        }
    public function editar($id){
        $cliente = Cliente::select(
        'cliente.id',
        'cliente.name',
        'cliente.telefone',
        'cliente.email',
        'endereco.cep',
        'endereco.uf',
        'endereco.cidade',
        'endereco.barrio',
        'endereco.rua',
        'endereco.numero',
        'endereco.complemento'
        )
        ->join('endereco','endereco.id','=','cliente.id_endereco')
        ->where('cliente.id','=',$id)
        ->get();
        return view("editar", compact("cliente"));
    }
    
    public function deletar($id){
        $cliente = Cliente::select('*')->find($id);
        $endereco = Endereco::find($cliente->id_endereco);
        $cliente->delete();
        return redirect("listar");
    }
}
