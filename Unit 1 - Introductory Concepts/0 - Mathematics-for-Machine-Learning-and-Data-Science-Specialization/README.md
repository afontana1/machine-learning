# [Mathematics for Machine Learning and Data Science Specialization](https://www.deeplearning.ai/courses/mathematics-for-machine-learning-and-data-science-specialization/)
Master the Toolkit of AI and Machine Learning. Mathematics for Machine Learning and Data Science is a beginner-friendly Specialization where you’ll learn the fundamental mathematics toolkit of machine learning: calculus, linear algebra, statistics, and probability.

## About this Specialization
Mathematics for Machine Learning and Data Science is a foundational online program created by DeepLearning.AI and taught by Luis Serrano. This beginner-friendly Specialization is where you’ll master the fundamental mathematics toolkit of machine learning.

Many machine learning engineers and data scientists need help with mathematics, and even experienced practitioners can feel held back by a lack of math skills. This Specialization uses innovative pedagogy in mathematics to help you learn quickly and intuitively, with courses that use easy-to-follow plugins and visualizations to help you see how the math behind machine learning actually works. 

This is a beginner-friendly program, with a recommended background of at least high school mathematics. We also recommend a basic familiarity with Python, as labs use Python to demonstrate learning objectives in the environment where they’re most applicable to machine learning and data science.

## Applied Learning Project
By the end of this Specialization, you will be ready to:
- Represent data as vectors and matrices and identify their properties using concepts of singularity, rank, and linear independence
- Apply common vector and matrix algebra operations like dot product, inverse, and determinants 
- Express certain types of matrix operations as linear transformations 
- Apply concepts of eigenvalues and eigenvectors to machine learning problems
- Optimize different types of functions commonly used in machine learning
- Perform gradient descent in neural networks with different activation and cost functions 
- Describe and quantify the uncertainty inherent in predictions made by machine learning models
- Understand the properties of commonly used probability distributions in machine learning and data science
- Apply common statistical methods like MLE and MAP
- Assess the performance of machine learning models using interval estimates and margin of errors 
- Apply concepts of statistical hypothesis testing

## Course 1: Linear Algebra for Machine Learning and Data Science
After completing this course, learners will be able to:
- Represent data as vectors and matrices and identify their properties using concepts of singularity, rank, and linear independence, etc.
- Apply common vector and matrix algebra operations like dot product, inverse, and determinants 
- Express certain types of matrix operations as linear transformations 
- Apply concepts of eigenvalues and eigenvectors to machine learning problems

### Week 1: Systems of Linear Equations
Matrices are commonly used in machine learning and data science to represent data and its transformations. In this week, you will learn how matrices naturally arise from systems of equations and how certain matrix properties can be thought in terms of operations on system of equations.

#### Learning Objectives
- Form and graphically interpret 2x2 and 3x3 systems of linear equations
- Determine the number of solutions to a 2x2 and 3x3 system of linear equations
- Distinguish between singular and non-singular systems of equations
- Determine the singularity of 2x2 and 3x3 system of equations by calculating the determinant

#### Lesson 1: Systems of Linear equations: two variables
- Machine learning motivation
- Systems of sentences
- Systems of equations
- Systems of equations as lines
- A geometric notion of singularity
- Singular vs nonsingular matrices
- Linear dependence and independence
- The determinant

#### Lesson 2: Systems of Linear Equations: three variables
- Systems of equations (3×3)
- Singular vs non-singular (3×3)
- Systems of equations as planes (3×3)
- Linear dependence and independence (3×3)
- The determinant (3×3)

### Week 2: Solving systems of Linear Equations
In this week, you will learn how to solve a system of linear equations using the elimination method and the row echelon form. You will also learn about an important property of a matrix: the rank. The concept of the rank of a matrix is useful in computer vision for compressing images.

#### Learning Objectives
- Solve a system of linear equations using the elimination method.
- Use a matrix to represent a system of linear equations and solve it using matrix row reduction.
- Solve a system of linear equations by calculating the matrix in the row echelon form.
- Calculate the rank of a system of linear equations and use the rank to determine the number of solutions of the system.

#### Lesson 1: Solving systems of Linear Equations: Elimination
- Machine learning motivation
- Solving non-singular systems of linear equations
- Solving singular systems of linear equations
- Solving systems of equations with more variables
- Matrix row-reduction
- Row operations that preserve singularity

#### Lesson 2: Solving systems of Linear Equations: Row Echelon Form and Rank
- The rank of a matrix
- The rank of a matrix in general
- Row echelon form
- Row echelon form in general
- Reduced row echelon form

### Week 3: Vectors and Linear Transformations
An individual instance (observation) of data is typically represented as a vector in machine learning. In this week, you will learn about properties and operations of vectors. You will also learn about linear transformations, matrix inverse, and one of the most important operations on matrices: the matrix multiplication. You will see how matrix multiplication naturally arises from composition of linear transformations. Finally, you will learn how to apply some of the properties of matrices and vectors that you have learned so far to neural networks.

#### Learning Objectives
- Perform common operations on vectors like sum, difference, and dot product.
- Multiply matrices and vectors.
- Represent a system of linear equations as a linear transformation on a vector.
- Calculate the inverse of a matrix, if it exists.

#### Lesson 1: Vectors
- Norm of a vector
- Sum and difference of vectors
- Distance between vectors
- Multiplying a vector by a scalar
- The dot product
- Geometric Dot Product
- Multiplying a matrix by a vector

#### Lesson 2: Linear transformations
- Matrices as linear transformations
- Linear transformations as matrices
- Matrix multiplication
- The identity matrix
- Matrix inverse
- Which matrices have an inverse?
- Neural networks and matrices

### Week 4: Determinants and Eigenvectors
In this final week, you will take a deeper look at determinants. You will learn how determinants can be geometrically interpreted as an area and how to calculate determinant of product and inverse of matrices. We conclude this course with eigenvalues and eigenvectors. Eigenvectors are used in dimensionality reduction in machine learning. You will see how eigenvectors naturally follow from the concept of eigenbases.

#### Learning Objectives
- Interpret the determinant of a matrix as an area and calculate determinant of an inverse of a matrix and a product of matrices.
- Determine the bases and span of vectors.
- Find eigenbases for a special type of linear transformations commonly used in machine learning.
- Calculate the eignenvalues and eigenvectors of a linear transformation (matrix).

#### Lesson 1: Determinants In-depth
- Machine Learning Motivation
- Singularity and rank of linear transformation
- Determinant as an area
- Determinant of a product
- Determinants of inverses

#### Lesson 2: Eigenvalues and Eigenvectors
- Bases in Linear Algebra
- Span in Linear Algebra
- Interactive visualization: Linear Span
- Eigenbases
- Eigenvalues and eigenvectors

## Course 2: Calculus for Machine Learning and Data Science
After completing this course, learners will be able to:
- Analytically optimize different types of functions commonly used in machine learning using properties of derivatives and gradients
- Approximately optimize different types of functions commonly used in machine learning using first-order (gradient descent) and second-order (Newton’s method) iterative methods
- Visually interpret differentiation of different types of functions commonly used in machine learning
- Perform gradient descent in neural networks with different activation and cost functions 

### Week 1: Functions of one variable: Derivative and optimization

#### Lesson 1: Derivatives
- Example to motivate derivatives: Speedometer
- Derivative of common functions (c, x, x^2, 1/x)
- Meaning of e and the derivative of e^x
- Derivative of log x
- Existence of derivatives
- Properties of derivative

#### Lesson 2: Optimization with derivatives
- Intro to optimization: Temperature example
- Optimizing cost functions in ML: Squared loss
- Optimizing cost functions in ML: Log loss

### Week 2: Functions of two or more variables: Gradients and gradient descent

#### Lesson 1: Gradients and optimization
- Intro to gradients
- Example to motivate gradients: Temperature
- Gradient notation
- Optimization using slope method: Linear regression

#### Lesson 2: Gradient Descent
- Optimization using gradient descent: 1 variable
- Optimization using gradient descent: 2 variable
- Gradient descent for linear regression

### Week 3: Optimization in Neural Networks and Newton’s method

#### Lesson 1: Optimization in Neural Networks
- Perceptron with no activation and squared loss (linear regression)
- Perceptron with sigmoid activation and log loss (classification)
- Two-layer neural network with sigmoid activation and log loss
- Mathematics of Backpropagation

#### Lesson 2: Beyond Gradient Descent: Newton’s Method
- Root finding with Newton’s method
- Adapting Newton’s method for optimization
- Second derivatives and Hessians
- Multivariate Newton’s method

## Course 3: Probability & Statistics for Machine Learning & Data Science
After completing this course, learners will be able to:
- Analytically optimize different types of functions commonly used in machine learning using properties of derivatives and gradients 
- Approximately optimize different types of functions commonly used in machine learning using first-order (gradient descent) and second-order (Newton’s method) iterative methods
- Visually interpret differentiation of different types of functions commonly used in machine learning
- Perform gradient descent in neural networks with different activation and cost functions 

### Week 1: Introduction to probability and random variables

#### Lesson 1: Introduction to probability
- Concept of probability: repeated random trials
- Conditional probability and independence
- Discriminative learning and conditional probability
- Bayes theorem

#### Lesson 2: Random variables
- Random variables
- Cumulative distribution function
- Discrete random variables: Bernoulli distribution
- Discrete random variables: Binomial distribution
- Probability mass function
- Continuous random variables: Uniform distribution
- Continuous random variables: Gaussian distribution
- Continuous random variables: Chi squared distribution
- Probability distribution function

### Week 2: Describing distributions and random vectors

#### Lesson 1: Describing distributions
- Measures of central tendency: mean, median, mode
- Expected values
- Quantiles and box-plots
- Measures of dispersion: variance, standard deviation

#### Lesson 2: Random vectors
- Joint distributions
- Marginal and conditional distributions
- Independence
- Measures of relatedness: covariance
- Multivariate normal distribution

### Week 3: Introduction to statistics

#### Lesson 1: Sampling and point estimates
- Population vs. sample
- Describing samples: sample proportion and sample mean
- Distribution of sample mean and proportion: Central Limit Theorem
- Point estimates
- Biased vs Unbiased estimates

#### Lesson 2: Maximum likelihood estimation
- ML motivation example: Linear Discriminant Analysis
- Likelihood
- Intuition behind maximum likelihood estimation
- MLE: How to get the maximum using calculus

#### Lesson 3: Bayesian statistics
- ML motivation example: Naive Bayes
- Frequentist vs. Bayesian statistics
- A priori/ a posteriori distributions
- Bayesian estimators: posterior mean, posterior median, MAP

### Week 4: Interval statistics and Hypothesis testing

#### Lesson 1: Confidence intervals
- Margin of error
- Interval estimation
- Confidence Interval for mean of population
- CI for parameters in linear regression
- Prediction Interval

#### Lesson 2: Hypothesis testing
- ML Motivation: AB Testing
- Criminal trial
- Two types of errors
- Test for proportion and means
- Two sample inference for difference between groups
- ANOVA
- Power of a test

