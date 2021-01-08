// Find all Hamiltonian Cycle In A Graph


public class Graph_Find_All_Hamiltonian_Cycle {

    int [][]graph;
    int number_of_vertices;
    Graph_Find_All_Hamiltonian_Cycle(int vertices){
        this.number_of_vertices=vertices;
        this.graph=new int[vertices][vertices];
        for(int i=0;i<vertices;i++){
            for(int j=0;j<vertices;j++){
                this.graph[i][j]=-1;
            }
        }
    }

    private void Add_Edge(int src,int dest){
        this.graph[src][dest]=1;
        this.graph[dest][src]=1;
    }

    // private void Display_Matrix(){
    //     for(int []ar:this.graph){
    //         for(int x:ar){
    //             System.out.printf("%3d",x);
    //         }
    //         System.out.println();
    //     }
    // }

    private void Hamiltonian_Cycle(){
        int []path=new int[this.number_of_vertices];
        for(int i=0;i<this.number_of_vertices;i++){
            path[i]=-1;     //initially no vertex is processed
        }
        int start_vertex=0;
        path[0]=0;      //start vertex is processed
        Hamiltonian_Cycle_Util(path,1,start_vertex);  //Recursive call for next vertex
    } 

    private boolean is_Safe(int []path,int current_vertex,int adj_vertex) {
        //if there is no direct edge between adj_vertex and current_vertex
        if(this.graph[path[current_vertex-1]][adj_vertex]==-1){
            return false;
        }

        for(int i=0;i<current_vertex;i++) {
            //if the vertex adj_vertex is already processed
            if (path[i]==adj_vertex){
                return false;
            }
        }
        return true;
    }


    private void Hamiltonian_Cycle_Util(int []path,int current_vertex,int start_vertex){

        if(current_vertex==this.number_of_vertices){
            //if this is the last vertex of graph
            if(this.graph[path[current_vertex-1]][start_vertex]==1){
                System.out.println("Cycle:");
                for (int x:path){
                    System.out.print(x+" ");
                }
                System.out.print(start_vertex+"\n\n");
            }
            return;
        }

        for(int i=0;i<this.number_of_vertices;i++){
            //Adjacent Vertices
            if(is_Safe(path,current_vertex,i)){ //if i is adjacent to current_vertex
                path[current_vertex]=i;
                Hamiltonian_Cycle_Util(path,current_vertex+1,start_vertex); //Recursive call
                path[current_vertex]=-1;   //Backtrack
            }
        }


    }

    public static void main(String []args){
        int vertices=6;
        Graph_Find_All_Hamiltonian_Cycle hamil=new Graph_Find_All_Hamiltonian_Cycle(vertices);
        hamil.Add_Edge(0,1);
        hamil.Add_Edge(0,2);
        hamil.Add_Edge(0,5);
        hamil.Add_Edge(1,2);
        hamil.Add_Edge(1,4);
        hamil.Add_Edge(1,5);
        hamil.Add_Edge(2,3);
        hamil.Add_Edge(3,4);
        hamil.Add_Edge(4,5);
        hamil.Add_Edge(0,2);
        hamil.Add_Edge(0,3);
        hamil.Add_Edge(1,2);
        hamil.Add_Edge(1,4);
        hamil.Add_Edge(2,3);
        hamil.Add_Edge(2,4);
        hamil.Add_Edge(3,4);

        hamil.Hamiltonian_Cycle();
    }

}
