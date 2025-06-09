import matplotlib.pyplot as plt
import pandas as pd


def clean_time(col: pd.Series) -> float:
    """ Helper to clean 'Xs' to float seconds """
    return col.str.replace('s', '', regex=False).astype(float)

def compare_omp_mpi_strong_scaling_rayleigh_benard_2d() -> None:
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
    
def increasing_resolution_rayleigh_benard_2d() -> None:
    # Load the CSV file
    df = pd.read_csv("csv/RayleighBenard2d_Resolution_Increase_(12_threads_2_processes).csv")

    # Create the plot
    plt.figure(figsize=(12, 6))

    # Subplot 1: Real Time and CPU Time
    plt.subplot(1, 2, 1)
    plt.plot(df['Resolution'], df['Real Time'], color="purple", marker='o', label='Real Time (s)')
    plt.plot(df['Resolution'], df['CPU Time'], color="gold", marker='s', label='CPU Time (s)')
    plt.title('RayleighBenard2d: Time vs Resolution')
    plt.xlabel('Resolution')
    plt.ylabel('Time (s)')
    plt.legend()
    plt.grid(True)

    # Subplot 2: MLUP/s and MLUP/p/s
    plt.subplot(1, 2, 2)
    plt.plot(df['Resolution'], df['Avg MLUP/s'], color="purple", marker='^', label='Avg MLUP/s')
    plt.plot(df['Resolution'], df['Avg MLUP/p/s'], color="gold", marker='x', label='Avg MLUP/p/s')
    plt.title('RayleighBenard2d: Performance vs Resolution')
    plt.xlabel('Resolution')
    plt.ylabel('Performance')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()
    
def bifurcation3d_omp_weak_vs_strong() -> None:
    # Load the CSV files
    strong_df = pd.read_csv('csv/Bifurcation3d_OpenMP_Strong_Scaling.csv')
    weak_df = pd.read_csv('csv/Bifurcation3d_OpenMP_Weak_Scaling.csv')

    # Clean 's' and convert time columns to float
    for col in ['Real Time (1st)', 'Real Time (2nd)', 'CPU Time (1st)', 'CPU Time (2nd)']:
        strong_df[col] = strong_df[col].str.rstrip('s').astype(float)
        weak_df[col] = weak_df[col].str.rstrip('s').astype(float)

    # Calculate averages
    strong_df['Real Time Avg'] = (strong_df['Real Time (1st)'] + strong_df['Real Time (2nd)']) / 2
    weak_df['Real Time Avg'] = (weak_df['Real Time (1st)'] + weak_df['Real Time (2nd)']) / 2

    plt.figure(figsize=(10,6))

    # Plot strong scaling
    plt.plot(strong_df['OMP N Threads'], strong_df['Real Time Avg'], marker='o', color='purple', label='Strong Scaling')

    # Plot weak scaling
    plt.plot(weak_df['OMP N Threads'], weak_df['Real Time Avg'], marker='s', color='gold', label='Weak Scaling')

    # Add annotations on weak scaling points
    for _, row in weak_df.iterrows():
        plt.annotate(f"Res: {row['Resolution']}",  # text
                    (row['OMP N Threads'], row['Real Time Avg']),  # point (x, y)
                    textcoords="offset points",  # how to position text
                    xytext=(0,10),  # offset: 10 points vertical above
                    ha='center',  # horizontal alignment
                    fontsize=8,
                    color='black')

    plt.xlabel('OMP N Threads')
    plt.ylabel('Average Real Time (s)')
    plt.title('Bifurcation3d Strong vs Weak Scaling with Resolution Annotations')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def main() -> None:
    """ Create charts and graphs based on CS 470 final project output """
    
    # Comparison of OpenMP and MPI average runtime for RayleighBenard2d
    compare_omp_mpi_strong_scaling_rayleigh_benard_2d() 
    
    # Chart showing the effects of increasing the resolution for RayleighBenard2d
    increasing_resolution_rayleigh_benard_2d()
    
    # Chart comparing strong vs weak scaling for Birfurcation3d
    bifurcation3d_omp_weak_vs_strong()

if __name__ == "__main__":
    main()
