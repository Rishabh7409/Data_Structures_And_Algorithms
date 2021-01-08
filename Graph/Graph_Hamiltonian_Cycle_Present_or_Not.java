

public class Graph_Hamiltonian_Cycle_Present_or_Not {

    int [][]graph;
    int number_of_vertices;
    
    Graph_Hamiltonian_Cycle_Present_or_Not(int vertices){
        this.number_of_vertices=vertices;
        
        // store graph in form of adjacency matrix 
        this.graph=new int[vertices][vertices];
        for(int i=0;i<vertices;i++){
            for(int j=0;j<vertices;j++){
                // initially all the blocks will be -1
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

    private boolean Hamiltonian_Cycle(){
        int []path=new int[this.number_of_vertices];
        for(int i=0;i<this.number_of_vertices;i++){
            path[i]=-1;
        }
        // take any start vertex
        int start_vertex=0;
        
        // put start_vertex in path array 
        path[0]=start_vertex;
        
        return Hamiltonian_Cycle_Util(path,1,start_vertex);
    }

    private boolean is_Safe(int []path,int pos,int num) {

        // pos represents current index in path array
        // num represents starting vertex of cycle
        // path array stores hamiltonian cycle

        // if there is no direct edge between the vertices
        if(this.graph[path[pos-1]][num]==-1){
            return false;
        }

        // if current vertex is not visited yet return true else return false
        for(int i=0;i<pos;i++) {
            if (path[i]==num){
                return false;
            }
        }
        return true;
    }


    private boolean Hamiltonian_Cycle_Util(int []path,int pos,int start_vertex){

        if(pos==this.number_of_vertices) {
            // if there is an edge from last vertex to source vertex
            if (this.graph[path[pos - 1]][start_vertex] == 1) {
                return true;
            }
        }

        for(int i=0;i<this.number_of_vertices;i++){
            if(is_Safe(path,pos,i)){
                path[pos]=i;
                if(Hamiltonian_Cycle_Util(path,pos+1,start_vertex)){
                    return true;
                }
                // backtracking
                path[pos]=-1;
            }
        }

        return false;
    }

    public static void main(String []args){
        int total_vertices=6;
        Graph_Hamiltonian_Cycle_Present_or_Not hamil=new Graph_Hamiltonian_Cycle_Present_or_Not(total_vertices);
        hamil.Add_Edge(0,1);
        hamil.Add_Edge(0,2);
        hamil.Add_Edge(0,5);
        hamil.Add_Edge(1,2);
        hamil.Add_Edge(1,4);
        hamil.Add_Edge(1,5);
        hamil.Add_Edge(2,3);
        hamil.Add_Edge(3,4);
        hamil.Add_Edge(4,5);

        

        // hamil.Display_Matrix();

        boolean cycle_present=hamil.Hamiltonian_Cycle();
        System.out.println(cycle_present?"\nYes,Hamiltonian Cycle Exists":"\nNo Hamiltonian Cycle Exists");
    }

}
