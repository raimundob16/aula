<table class="table">
    <thead>
      <tr>
        <th scope="col">#</th>
        <th scope="col">Nome</th>
        <th scope="col">Telefone</th>
        <th scope="col">Email</th>
        <th scope="col">Rua</th>
        <th scope="col">Numero</th>

      </tr>
    </thead>
    <tbody>
        @foreach ($cliente as $cliente)
            
      
      <tr>
        <th scope="row">{{$cliente->id}}</th>
        <td>{{$cliente->name}}</td>
        <td>{{$cliente->telefone}}</td> 
        <td>{{$cliente->email}}</td>
        <td> <a href="{{route('editar',$cliente->id)}}"><button type="button" class="btn btn-primary">Editar</button></a></td>
        <td> <a href="{{route('deletar',$cliente->id)}}"><button type="button" class="btn btn-primary">Deletar</button></a></td>
        
       
      </tr>
      @endforeach
      
    </tbody>
  </table>