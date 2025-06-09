import matplotlib.pyplot as plt
import pandas as pd

def compare_omp_mpi_strong_scaling_rayleigh() -> None:
    # Load MPI data
    mpi_df = pd.read_csv("csv/RayleighBenard2d_MPI_Strong _Scaling.csv")
    
    # Remove 's' and convert Real Time to float
    mpi_df['Real Time (1st)'] = mpi_df['Real Time (1st)'].str.replace('s', '').astype(float)
    mpi_df['Real Time (2nd)'] = mpi_df['Real Time (2nd)'].str.replace('s', '').astype(float)
    
    # Average the two runtimes to make the graph easier to read
    mpi_df['Real Time Avg'] = (mpi_df['Real Time (1st)'] + mpi_df['Real Time (2nd)']) / 2
    
    # Load OpenMP data and do the same
    omp_df = pd.read_csv("csv/RayleighBenard2d_OMP_Strong_Scaling.csv")
    omp_df['Real Time (1st)'] = omp_df['Real Time (1st)'].str.replace('s', '').astype(float)
    omp_df['Real Time (2nd)'] = omp_df['Real Time (2nd)'].str.replace('s', '').astype(float)
    omp_df['Real Time Avg'] = (omp_df['Real Time (1st)'] + omp_df['Real Time (2nd)']) / 2
    
    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(mpi_df['N Processes'], mpi_df['Real Time Avg'], marker='o', label='MPI (Avg Real Time)', color='purple')
    plt.plot(omp_df['OMP N Threads'], omp_df['Real Time Avg'], marker='s', label='OpenMP (Avg Real Time)', color='gold')

    plt.xlabel("Threads / Processes")
    plt.ylabel("Average Real Time (s)")
    plt.title("RayleighBenard2d Strong Scaling: Avg Real Time (MPI vs OpenMP)")
    plt.grid(True)
    plt.legend()
    plt.xticks(mpi_df['N Processes'])
    plt.tight_layout()
    plt.show()


def main() -> None:
    """ Create charts and graphs based on CS 470 final project output """
    
    #Comparison of OpenMP and MPI Average Runtime for RayleighBenard2d
    compare_omp_mpi_strong_scaling_rayleigh()

if __name__ == "__main__":
    main()
